def transpose(lines):
    # Get the maximum length of any line in the input
    max_length = max(len(line) for line in lines) if lines else 0

    # Pad the lines with spaces to make them equal length
    padded_lines = [line.ljust(max_length) for line in lines]

    # Transpose the lines
    transposed_lines = [''.join(line) for line in zip(*padded_lines)]

    return transposed_lines
