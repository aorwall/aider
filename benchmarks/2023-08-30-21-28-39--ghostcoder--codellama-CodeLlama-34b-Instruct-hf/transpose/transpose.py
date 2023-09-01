def transpose(lines):
    # Calculate the maximum length of the input lines
    max_length = max(len(line) for line in lines)

    # Initialize an empty list to store the transposed lines
    transposed_lines = []

    # Loop through each line in the input
    for line in lines:
        # Pad the line with spaces to the left to match the maximum length
        padded_line = line.rjust(max_length)

        # Split the padded line into a list of characters
        char_list = list(padded_line)

        # Add the list of characters to the transposed lines list
        transposed_lines.append(char_list)

    # Return the transposed lines list
    return transposed_lines
