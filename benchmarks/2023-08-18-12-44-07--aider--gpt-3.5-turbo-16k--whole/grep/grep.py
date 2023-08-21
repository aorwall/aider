import re

def grep(pattern, flags, files):
    # Initialize an empty list to store the matching lines
    matching_lines = []

    # Compile the pattern with the appropriate flags
    compiled_pattern = re.compile(pattern, re.IGNORECASE if '-i' in flags else 0)

    # Iterate over each file
    for file in files:
        try:
            # Open the file for reading
            with open(file, 'r') as f:
                # Read all lines from the file
                lines = f.readlines()

                # Iterate over each line
                for line_number, line in enumerate(lines, start=1):
                    # Apply the flags
                    if '-x' in flags:
                        # Match the entire line
                        if re.fullmatch(compiled_pattern, line):
                            matching_lines.append(f'{file}:{line_number}:{line}')
                    elif '-v' in flags:
                        # Invert the match
                        if not re.search(compiled_pattern, line):
                            matching_lines.append(f'{file}:{line_number}:{line}')
                    else:
                        # Perform normal matching
                        if re.search(compiled_pattern, line):
                            matching_lines.append(f'{file}:{line_number}:{line}')
        except FileNotFoundError:
            # Handle file not found error
            print(f'File not found: {file}')

    # Return the matching lines
    return matching_lines
