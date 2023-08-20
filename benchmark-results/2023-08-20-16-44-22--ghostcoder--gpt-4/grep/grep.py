import re
import os

def grep(pattern, flags, files):
    results = []
    line_number = '-n' in flags
    file_names_only = '-l' in flags
    case_insensitive = '-i' in flags
    invert = '-v' in flags
    whole_line = '-x' in flags

    if case_insensitive:
        pattern = pattern.lower()

    for file in files:
        with open(file, 'r') as f:
            for i, line in enumerate(f, start=1):
                search_line = line.lower() if case_insensitive else line
                match = re.fullmatch(pattern, search_line.strip()) if whole_line else re.search(pattern, search_line)
                if (match and not invert) or (not match and invert):
                    if file_names_only:
                        results.append(file)
                        break
                    prefix = f"{file}:{i}:" if line_number else f"{file}:"
                    results.append(f"{prefix}{line.strip()}")
    return "\n".join(results)