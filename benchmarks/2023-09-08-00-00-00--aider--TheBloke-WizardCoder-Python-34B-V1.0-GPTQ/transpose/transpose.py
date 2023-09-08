def transpose(lines):
    if not lines:
        return []

    max_length = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_length) for line in lines]
    transposed_lines = [''.join(line[i] for line in padded_lines) for i in range(max_length)]
    return transposed_lines
