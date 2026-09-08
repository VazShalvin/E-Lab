# Standard library
import os
import re
import shlex
import shutil
import subprocess
import uuid
import base64


def _detect_host_sandbox_dir(container_dir):
    """
    Detect the host path backing container_dir for Docker-out-of-Docker / sibling containers.
    1. Returns HOST_SANDBOX_DIR environment variable if explicitly set and not container_dir.
    2. Parses /proc/self/mountinfo to detect the underlying host bind-mount path.
    3. Falls back to HOST_SANDBOX_DIR or container_dir.
    """
    env_dir = os.environ.get("HOST_SANDBOX_DIR")
    if env_dir and env_dir != container_dir:
        return env_dir

    try:
        if os.path.exists("/proc/self/mountinfo"):
            with open("/proc/self/mountinfo", "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 5 and parts[4] == container_dir:
                        host_path = parts[3]
                        if os.path.isabs(host_path) and host_path != container_dir:
                            return host_path
    except Exception:
        pass

    return env_dir or container_dir


SANDBOX_DIR = os.environ.get("DOCKER_SANDBOX_DIR", "/var/elab-sandbox")
SANDBOX_IMAGE = os.environ.get("DOCKER_SANDBOX_IMAGE", "elab-sandbox")
HOST_SANDBOX_DIR = _detect_host_sandbox_dir(SANDBOX_DIR)

# Marker emitted by the inner script when compilation fails. Picked to be
# impossible to appear in normal program output.
_COMPILE_ERROR_MARKER = "__ELAB_COMPILE_ERROR__"


# Each language maps to:
#   - monaco:    the Monaco editor language id used in the browser
#   - filename:  the source filename written into the box
#   - compile:   list[str] compile command (None for interpreted languages)
#   - run:       list[str] run command (run after a successful compile)
#
# For C/C++ we keep -Wall/-Wextra so warnings are visible, but only hard-fail
# on correctness issues that bite beginners (missing `return`, bad `main`).
# Java's class name is resolved at run time (see _java_filename) so students
# never hit a "public class X must be defined in X.java" error.
LANGUAGES = {
    "c": {
        "monaco": "c",
        "filename": "main.c",
        "compile": [
            "gcc", "-Wall", "-Wextra",
            "-Werror=return-type", "-Werror=main",
            "-std=c11", "-O2", "-o", "program", "main.c",
        ],
        "run": ["./program"],
    },
    "cpp": {
        "monaco": "cpp",
        "filename": "main.cpp",
        "compile": [
            "g++", "-Wall", "-Wextra",
            "-Werror=return-type", "-Werror=main",
            "-std=c++17", "-O2", "-o", "program", "main.cpp",
        ],
        "run": ["./program"],
    },
    "python": {
        "monaco": "python",
        "filename": "main.py",
        "compile": None,
        "run": ["python3", "main.py"],
    },
    "java": {
        "monaco": "java",
        "filename": "__AUTO__",  # resolved per-submission via _java_filename
        "compile": ["javac", "__SOURCE__"],
        "run": ["java", "__CLASS__"],
    },
    "sql": {
        "monaco": "sql",
        "filename": "main.sql",
        "compile": ["sh", "-c", "cat input.txt __SOURCE__ > combined.sql"],
        "run": ["sqlite3", "-batch", "test.db", ".read combined.sql"],
    },
}

# Maps the Question/Submission `language_id` to a language
# key above. 50 (C) stays the default for backwards compatibility.
LANGUAGE_ID_MAP = {
    50: "c",
    54: "cpp",
    62: "java",
    71: "python",
    82: "sql",
}


def language_for_id(language_id):
    """Resolve a Question/Submission language_id to a registry key (default: c)."""
    return LANGUAGE_ID_MAP.get(int(language_id or 50), "c")


def _java_filename(source_code):
    """
    Detect the Java class name so the source file is saved under the matching
    name (required by javac for public classes). Order:
      1. first `public class X`
      2. first `class X` (non-public)
      3. fallback to "Main"
    """
    # Match public class possibly preceded by modifiers like abstract/final
    match = re.search(r"\b(?:public\s+)?(?:abstract\s+)?(?:final\s+)?class\s+(\w+)", source_code)
    if not match:
        match = re.search(r"\b(?:public\s+)?(?:abstract\s+)?(?:final\s+)?class\s+(\w+)", source_code)
    name = match.group(1) if match else "Main"
    return name + ".java", name


def _write_file_safe(path, content):
    """Write content to a file using base64 to avoid shell escaping issues."""
    encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
    # Use a temp file approach: decode inside the container script
    return encoded


def _build_inner_script(lang_config, source_filename, class_name, time_limit, source_code=None, stdin=""):
    """
    Build the sh -c script that runs inside the container. It compiles first
    (emitting our marker on failure), then runs the program under `timeout`.
    Splitting the phases lets us distinguish compile errors from runtime errors
    definitively instead of sniffing output for "error:".
    """
    parts = [
        "touch /tmp/input.txt",
        "cd /tmp",
        "touch input.txt",
    ]

    # Write source code using base64 encoding to avoid heredoc/escaping issues
    if source_code is not None:
        encoded_source = base64.b64encode(source_code.encode('utf-8')).decode('ascii')
        parts.append(f"echo '{encoded_source}' | base64 -d > {shlex.quote(source_filename)}")

    # Write stdin to input.txt using base64 encoding if provided
    if stdin:
        encoded_stdin = base64.b64encode(stdin.encode('utf-8')).decode('ascii')
        parts.append(f"echo '{encoded_stdin}' | base64 -d > input.txt")

    compile_cmd = lang_config["compile"]
    if compile_cmd is not None:
        resolved = []
        for token in compile_cmd:
            token = token.replace("__SOURCE__", source_filename)
            resolved.append(token)
        quoted = " ".join(shlex.quote(t) for t in resolved)
        # Compile output goes to compile.out; on failure, emit the marker and
        # the real compiler message, then exit 3.
        parts.append(
            f"if {quoted} >compile.out 2>&1; then "
            f"cp compile.out /box/ 2>/dev/null || true; "
            f"else "
            f"echo {_COMPILE_ERROR_MARKER}; cat compile.out; cp compile.out /box/ 2>/dev/null || true; exit 3; "
            f"fi"
        )

    run_cmd = list(lang_config["run"])
    run_cmd = [t.replace("__CLASS__", class_name) for t in run_cmd]
    quoted_run = " ".join(shlex.quote(t) for t in run_cmd)

    # Use timeout to enforce time limits. Fall back to stdbuf for unbuffered output.
    # Order: stdbuf (if available) -> timeout -> command
    parts.append(
        f"(command -v stdbuf >/dev/null 2>&1 && stdbuf -o0 timeout {time_limit}s {quoted_run} < input.txt) "
        f"|| (timeout {time_limit}s {quoted_run} < input.txt)"
    )

    return "; ".join(parts)


def run_code(language, source_code, stdin="", expected_output="",
             time_limit=2.0, memory_limit_kb=128000):
    """
    Run source code of the given language in an isolated Docker container.

    Returns a dict with: status_id, status, stdout, stderr, compile_output,
    time, memory. status_id values:
      3  Accepted, 4 Wrong Answer, 5 Time Limit Exceeded,
      6  Compilation Error, 11 Runtime Error
    """
    lang_key = LANGUAGES.get(language, LANGUAGES["c"])
    memory_limit_mb = max(16, int(memory_limit_kb) // 1024)
    run_id = str(uuid.uuid4())
    tmpdir = os.path.join(SANDBOX_DIR, run_id)
    host_sandbox_dir = _detect_host_sandbox_dir(SANDBOX_DIR)
    host_tmpdir = os.path.join(host_sandbox_dir, run_id)

    # Ensure tmpdir is unique and safe.
    # Since SANDBOX_DIR is bind-mounted from host_sandbox_dir, creating tmpdir
    # automatically creates host_tmpdir on the host.
    os.makedirs(tmpdir, exist_ok=True)
    if host_tmpdir == tmpdir:
        os.makedirs(host_tmpdir, exist_ok=True)

    class_name = ""
    if language == "java":
        source_filename, class_name = _java_filename(source_code)
    else:
        source_filename = lang_key["filename"]

    # Ensure source_filename is a string
    source_filename = str(source_filename)

    try:
        try:
            os.chmod(tmpdir, 0o777)
        except OSError:
            pass

        inner_script = _build_inner_script(lang_key, source_filename, class_name, time_limit, source_code, stdin)

        # Write the inner script to a file in the container's tmpdir
        script_path = os.path.join(tmpdir, "run_script.sh")
        with open(script_path, "w") as f:
            f.write("#!/bin/sh\n")
            f.write(inner_script)
        os.chmod(script_path, 0o755)

        # The script will be accessible at /box/run_script.sh in the container
        cmd = [
            "docker", "run", "--rm",
            "--network", "none",
            "--memory", f"{memory_limit_mb}m",
            "--memory-swap", f"{memory_limit_mb}m",
            "--cpus", "0.5",
            "--pids-limit", "64",
            "--cap-drop", "ALL",
            "--security-opt", "no-new-privileges:true",
            "--tmpfs", "/tmp:rw,nosuid,exec,size=50m",
            "-v", f"{host_tmpdir}:/box:rw",
            SANDBOX_IMAGE,
            "/box/run_script.sh",
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=time_limit + 10,
                check=False,
            )

            stdout = (result.stdout or "").strip()
            stderr = (result.stderr or "").strip()
            # Compile output may also have been written to compile.out in the
            # mounted box dir; prefer the streamed marker+body, fall back to file.
            compile_out_path = os.path.join(tmpdir, "compile.out")
            compile_file_output = ""
            if os.path.exists(compile_out_path):
                with open(compile_out_path, "r") as f:
                    compile_file_output = f.read().strip()

            # --- Compilation error: marker present or compile.out has errors ---
            if _COMPILE_ERROR_MARKER in stdout or _COMPILE_ERROR_MARKER in stderr:
                compile_msg = stdout.replace(_COMPILE_ERROR_MARKER, "").strip()
                if not compile_msg:
                    compile_msg = compile_file_output
                return {
                    "status_id": 6,
                    "status": "Compilation Error",
                    "stdout": "",
                    "stderr": "",
                    "compile_output": compile_msg or "Compilation failed.",
                    "time": "0.0",
                    "memory": 0,
                }

            # If a compiled language produced compile.out with errors but the
            # marker somehow didn't surface (defensive), still treat as CE.
            if lang_key["compile"] and compile_file_output and (
                "error:" in compile_file_output.lower()
            ):
                return {
                    "status_id": 6,
                    "status": "Compilation Error",
                    "stdout": "",
                    "stderr": "",
                    "compile_output": compile_file_output,
                    "time": "0.0",
                    "memory": 0,
                }

            # --- Time Limit Exceeded ---
            if result.returncode == 124 or "timeout" in stderr.lower():
                return {
                    "status_id": 5,
                    "status": "Time Limit Exceeded",
                    "stdout": stdout,
                    "stderr": stderr or "Execution timed out",
                    "compile_output": "",
                    "time": str(time_limit),
                    "memory": memory_limit_kb,
                }

            # --- Runtime Error ---
            if result.returncode != 0:
                detail = stderr or f"Process exited with code {result.returncode}."
                return {
                    "status_id": 11,
                    "status": "Runtime Error",
                    "stdout": stdout,
                    "stderr": detail,
                    "compile_output": "",
                    "time": "0.1",
                    "memory": 1024,
                }

            # --- Success path: compare against expected output ---
            expected = (expected_output or "").strip()
            if expected and stdout == expected:
                status_id, status_desc = 3, "Accepted"
            elif expected:
                status_id, status_desc = 4, "Wrong Answer"
            else:
                status_id, status_desc = 3, "Accepted"

            return {
                "status_id": status_id,
                "status": status_desc,
                "stdout": stdout,
                "stderr": stderr,
                "compile_output": compile_file_output,
                "time": "0.1",
                "memory": 1024,
            }

        except subprocess.TimeoutExpired:
            return {
                "status_id": 5,
                "status": "Time Limit Exceeded",
                "stdout": "",
                "stderr": "Execution timed out",
                "compile_output": "",
                "time": str(time_limit),
                "memory": memory_limit_kb,
            }

    except Exception:
        # On any unexpected error (e.g. docker daemon unreachable), return
        # INTERNAL_ERROR so the frontend can show a helpful message.
        return {
            "status_id": 11,
            "status": "Runtime Error",
            "stdout": "",
            "stderr": "Sandbox execution failed (docker unavailable or error).",
            "compile_output": "",
            "time": "0.0",
            "memory": 0,
        }
    finally:
        # Clean up tmpdir; removing tmpdir automatically removes files from host_tmpdir
        try:
            shutil.rmtree(tmpdir, ignore_errors=True)
        except Exception:
            pass
        if host_tmpdir == tmpdir:
            try:
                shutil.rmtree(host_tmpdir, ignore_errors=True)
            except Exception:
                pass


def run_c_code(source_code, stdin="", expected_output="",
               time_limit=2.0, memory_limit_kb=128000):
    """Backwards-compatible wrapper around run_code for C submissions."""
    return run_code(
        "c",
        source_code=source_code,
        stdin=stdin,
        expected_output=expected_output,
        time_limit=time_limit,
        memory_limit_kb=memory_limit_kb,
    )


def inject_headers(source_code, starter_code):
    """Prepend #include and import statements from starter_code if missing in source_code."""
    if not starter_code or not source_code:
        return source_code

    injected_lines = []

    for line in starter_code.splitlines():
        line_stripped = line.strip()
        if line_stripped.startswith("#include") or line_stripped.startswith("import "):
            # Only inject if the exact line is not already present
            if line_stripped not in source_code:
                # Also check for near-duplicates (ignore whitespace differences)
                normalized = re.sub(r'\s+', ' ', line_stripped)
                found = False
                for existing_line in source_code.splitlines():
                    if re.sub(r'\s+', ' ', existing_line.strip()) == normalized:
                        found = True
                        break
                if not found:
                    injected_lines.append(line_stripped)

    if injected_lines:
        return "\n".join(injected_lines) + "\n\n" + source_code
    return source_code
