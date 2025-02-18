def grep(pattern, flags, files):
    """
    Search files for lines matching a search string and return all matching lines.
    
    Args:
        pattern (str): The string to search for.
        flags (list[str]): Zero or more flags for customizing the command's behavior.
        files (list[str]): One or more files to search in.
    
    Returns:
        list[str]: The matching lines in the order in which they were found.
    """
    # Initialize variables
    lines = []
    line_number = 1
    filename = None

    # Iterate over files
    for file in files:
        # Open file and read lines
        with open(file, 'r') as f:
            for line in f:
                # Check if line matches pattern
                if pattern in line:
                    # Add line to lines list
                    lines.append(line)

                    # Check if line number flag is set
                    if '-n' in flags:
                        # Add line number to line
                        line = f'{line_number}: {line}'

                    # Check if filename flag is set
                    if '-l' in flags:
                        # Add filename to line
                        line = f'{file}: {line}'

                    # Check if case-insensitive flag is set
                    if '-i' in flags:
                        # Convert line to lowercase
                        line = line.lower()

                    # Check if invert flag is set
                    if '-v' in flags:
                        # Invert line
                        line = line[::-1]

                    # Check if exact match flag is set
                    if '-x' in flags:
                        # Check if line matches pattern exactly
                        if line == pattern:
                            # Add line to lines list
                            lines.append(line)

                    # Increment line number
                    line_number += 1

    # Return lines
    return lines
