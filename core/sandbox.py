# Standard library
import os
import re
import shlex
import shutil
import subprocess
import uuid


SANDBOX_DIR = os.environ.get("DOCKER_SANDBOX_DIR", "/var/elab-sandbox")
SANDBOX_IMAGE = os.environ.get("DOCKER_SANDBOX_IMAGE", "elab-sandbox")
HOST_SANDBOX_DIR = os.environ.get("HOST_SANDBOX_DIR", SANDBOX_DIR)

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
}

# Maps the Question/Submission `language_id` to a language
# key above. 50 (C) stays the default for backwards compatibility.
LANGUAGE_ID_MAP = {
    50: "c",
    54: "cpp",
    62: "java",
    71: "python",
}


def language_for_id(language_id):
    """Resolve a Question/Submission language_id to a registry key (default: c)."""
    return LANGUAGE_ID_MAP.get(int(language_id or 50), "c")


def _java_filename(source_code):
    """
    Detect the Java class name so the source file is saved under the matching
    name (required by javac for public classes). Order:
      1. first `public class X`
      2. first `class X`
      3. fallback to "Main"
    """
    match = re.search(r"\bpublic\s+class\s+(\w+)", source_code)
    if not match:
        match = re.search(r"\bclass\s+(\w+)", source_code)
    name = match.group(1) if match else "Main"
    return name + ".java", name


def _build_inner_script(lang_config, source_filename, class_name, time_limit):
    """
    Build the sh -c script that runs inside the container. It compiles first
    (emitting our marker on failure), then runs the program under `timeout`.
    Splitting the phases lets us distinguish compile errors from runtime errors
    definitively instead of sniffing output for "error:".
    """
    parts = [
        "cp -a /box/. /tmp/",
        "cd /tmp"
    ]

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
            f"{{ {quoted} >compile.out 2>&1; cp compile.out /box/ 2>/dev/null; }} || "
            f"{{ echo {_COMPILE_ERROR_MARKER}; cat compile.out; cp compile.out /box/ 2>/dev/null; exit 3; }}"
        )

    run_cmd = list(lang_config["run"])
    run_cmd = [t.replace("__CLASS__", class_name) for t in run_cmd]
    quoted_run = " ".join(shlex.quote(t) for t in run_cmd)
    parts.append(f"timeout {time_limit}s {quoted_run} < input.txt")

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
    host_tmpdir = os.path.join(HOST_SANDBOX_DIR, run_id)
    os.makedirs(tmpdir, exist_ok=True)

    class_name = ""
    if language == "java":
        source_filename, class_name = _java_filename(source_code)
    else:
        source_filename = lang_key["filename"]
    
    # Ensure source_filename is a string
    source_filename = str(source_filename)

    try:
        code_file = os.path.join(tmpdir, source_filename)
        with open(code_file, "w") as f:
            f.write(source_code)

        input_file = os.path.join(tmpdir, "input.txt")
        with open(input_file, "w") as f:
            f.write(stdin or "")

        inner_script = _build_inner_script(lang_key, source_filename, class_name, time_limit)

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
            "sh", "-c", inner_script,
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=time_limit + 5,
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

    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


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
