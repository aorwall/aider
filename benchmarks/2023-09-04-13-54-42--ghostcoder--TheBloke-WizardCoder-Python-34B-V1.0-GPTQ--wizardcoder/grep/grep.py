import os
import re
from typing import List

def grep(pattern: str, flags: List[str], files: List[str]) -> List[str]:
    results = []

    # Check if pattern should be treated as regex or literal string
    is_regex = not ('-x' in flags)

    # Convert pattern to lowercase if -i flag is provided
    if '-i' in flags:
        pattern = pattern.lower()

    # Loop through each file
    for fname in files:
        try:
            with open(fname, 'r', encoding='utf8') as file:
                # Read lines from file
                lines = file.readlines()

                # Loop through each line
                for index, line in enumerate(lines):
                    # Remove newline character at end of line
                    line = line.strip('\n')

                    # Check if line contains pattern
                    if is_regex:
                        matched = bool(re.search(pattern, line))
                    else:
                        matched = pattern in line

                    # If line matches pattern and -v flag is not provided
                    if matched and '-v' not in flags:
                        # Add line to results list
                        if '-n' in flags:
                            results.append(f"{os.path.basename(fname)}:{index+1}: {line}")
                        elif '-l' in flags:
                            results.append(f"{os.path.basename(fname)}")
                        else:
                            results.append(line)
                    elif not matched and '-v' in flags:
                        # Add line to results list
                        if '-n' in flags:
                            results.append(f"{os.path.basename(fname)}:{index+1}: {line}")
                        else:
                            results.append(line)
        except FileNotFoundError:
            print(f"grep: {fname}: No such file or directory")

    return results