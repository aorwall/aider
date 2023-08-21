def transpose(text):
    # Split the input text into lines
    lines = text.split('\n')

    # Get the maximum length of any line in the input
    max_length = max(len(line) for line in lines)

    # Pad each line with spaces to make them all the same length
    padded_lines = [line.ljust(max_length) for line in lines]

    # Transpose the lines by swapping rows and columns
    transposed_lines = [''.join(row) for row in zip(*padded_lines)]

    return transposed_lines