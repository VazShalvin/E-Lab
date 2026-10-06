import os
import django
import re
import sys

sys.path.append('/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import TestCase

def clean_value(s):
    if not s:
        return s
    
    # Remove variable assignments: "varname = "
    cleaned = re.sub(r'\b[a-zA-Z_0-9]+\s*=\s*', '', s)
    
    # The user requested: "just numbers no commas no brackets until and unless it is explicitly need"
    # To do this safely, we can replace `[`, `]`, and `,` with spaces, except when inside quotes.
    # We will iterate character by character.
    
    parts = []
    current_part = ""
    in_quotes = False
    
    for char in cleaned:
        if char == '"':
            in_quotes = not in_quotes
            current_part += char
        elif not in_quotes:
            if char in '[],':
                current_part += ' '
            else:
                current_part += char
        else:
            current_part += char
            
    # Collapse multiple spaces into one, but preserve newlines
    final_lines = []
    for line in current_part.splitlines():
        line = re.sub(r'[ \t]+', ' ', line).strip()
        if line:
            final_lines.append(line)
            
    # For LeetCode, multiple arguments were previously joined by comma at top level
    # Since we replaced comma with space, they are now all space-separated.
    # So "nums = [1, 2], k = 3" -> "[1, 2], 3" -> "1 2 3"
    # If the user wants them separated by newlines, we should split them by comma BEFORE replacing comma with space.
    return "\n".join(final_lines)

def clean_value_v2(s):
    if not s:
        return s
    
    # 1. Remove varname = 
    s = re.sub(r'\b[a-zA-Z_0-9]+\s*=\s*', '', s)
    
    # 2. Split into arguments by top-level comma
    # Top-level comma means comma not inside brackets or quotes
    args = []
    current_arg = ""
    bracket_depth = 0
    in_quotes = False
    
    for char in s:
        if char == '"':
            in_quotes = not in_quotes
            current_arg += char
        elif not in_quotes:
            if char in '[{(':
                bracket_depth += 1
                current_arg += char
            elif char in ']})':
                bracket_depth -= 1
                current_arg += char
            elif char == ',' and bracket_depth == 0:
                args.append(current_arg.strip())
                current_arg = ""
            else:
                current_arg += char
        else:
            current_arg += char
            
    if current_arg:
        args.append(current_arg.strip())
        
    # 3. For each argument, replace brackets and commas with spaces, unless inside quotes
    final_args = []
    for arg in args:
        cleaned_arg = ""
        in_quotes_arg = False
        for char in arg:
            if char == '"':
                in_quotes_arg = not in_quotes_arg
                cleaned_arg += char
            elif not in_quotes_arg:
                if char in '[],':
                    cleaned_arg += ' '
                else:
                    cleaned_arg += char
            else:
                cleaned_arg += char
        # Collapse spaces
        cleaned_arg = re.sub(r'[ \t]+', ' ', cleaned_arg).strip()
        final_args.append(cleaned_arg)
        
    return "\n".join(final_args)


def main():
    testcases = TestCase.objects.all()
    updated = 0
    for tc in testcases:
        original_stdin = tc.stdin
        original_output = tc.expected_output
        
        new_stdin = clean_value_v2(original_stdin) if original_stdin else original_stdin
        new_output = clean_value_v2(original_output) if original_output else original_output
        
        if new_stdin != original_stdin or new_output != original_output:
            tc.stdin = new_stdin
            tc.expected_output = new_output
            tc.save(update_fields=['stdin', 'expected_output'])
            updated += 1
            
    print(f"Updated {updated} test cases to no-bracket, no-comma format.")

if __name__ == "__main__":
    main()
