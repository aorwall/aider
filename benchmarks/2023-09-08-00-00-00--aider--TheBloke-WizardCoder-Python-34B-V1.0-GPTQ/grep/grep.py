import re
import os

def grep(pattern, flags, files):
    invert = '-v' in flags
    case_insensitive = '-i' in flags
    exact_match = '-x' in flags
    output_line_numbers = '-n' in flags
    output_file_names = '-l' in flags

    if case_insensitive:
        pattern = re.compile(pattern, re.IGNORECASE)
    else:
        pattern = re.compile(pattern)

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line_number = i + 1
                line = line.strip()
                match = pattern.search(line)
                if (not exact_match and match) or (exact_match and match and match.group(0) == line):
                    if invert:
                        continue
                    if output_line_numbers:
                        line = f"{file}:{line_number}:{line}"
                    else:
                        line = f"{file}:{line}"
                    return line
                elif invert and not match:
                    if output_file_names:
                        return file
                    elif output_line_numbers:
                        line = f"{file}:{line_number}:{line}"
                    else:
                        line = f"{file}:{line}"
                    return line
