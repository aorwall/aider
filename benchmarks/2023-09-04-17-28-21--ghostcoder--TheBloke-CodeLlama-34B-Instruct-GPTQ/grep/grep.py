import re
from typing import List

def grep(pattern: str, flags: List[str], files: List[str]) -> None:
    """Simplified implementation of the grep command."""
    # Compile the pattern into a regex object
    regex = re.compile(pattern)

    # Iterate over the input files
    for file in files:
        # Open the file and read its content
        with open(file, 'r') as f:
            content = f.read()

        # Find all occurrences of the pattern in the file
        matches = []
        for m in regex.finditer(content):
            # If -x flag is set, check if the whole line matches the pattern
            if '-x' in flags and m.start() != 0 and m.end() != len(content):
                continue

            # Add the matched line to the list of matches
            matches.append((m.start(), m.end()))

        # Print the results according to the selected flags
        if '-l' in flags:
            print(f"{file}:")
        elif '-n' in flags:
            for start, end in matches:
                print(f"{file}:{start+1}:{content[start:end]}")
        else:
            for start, end in matches:
                print(content[start:end])