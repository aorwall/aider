import re

def grep(pattern, flags, files):
    # Initialize an empty list to store the matching lines
    matching_lines = []

    # Iterate over each file
    for file in files:
        # Open the file in read mode
        with open(file, 'r') as f:
            # Read all lines from the file
            lines = f.readlines()

            # Iterate over each line
            for line_number, line in enumerate(lines, start=1):
                # Remove the newline character from the end of the line
                line = line.rstrip('\n')

                # Check if the line matches the pattern based on the flags
                if match_line(line, pattern, flags):
                    # If the line matches, append it to the matching lines list
                    matching_lines.append(format_line(line, file, line_number, flags))

    # Return the matching lines
    return matching_lines


def match_line(line, pattern, flags):
    # Check if the line matches the pattern based on the flags
    if '-x' in flags:
        # If the -x flag is present, check if the line matches the entire pattern
        return line == pattern
    elif '-i' in flags:
        # If the -i flag is present, perform a case-insensitive comparison
        return re.search(pattern, line, re.IGNORECASE) is not None
    else:
        # Perform a case-sensitive comparison
        return re.search(pattern, line) is not None


def format_line(line, file, line_number, flags):
    # Format the line based on the flags
    if '-n' in flags:
        # If the -n flag is present, prepend the line number and a colon to the line
        line = f"{line_number}:{line}"
    if '-l' in flags:
        # If the -l flag is present, return only the file name
        return file
    else:
        # Prepend the file name and a colon to the line
        return f"{file}:{line}"