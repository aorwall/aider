def transpose(lines):
    if not lines:
        return ''

    max_len = max([len(line) for line in lines])
    padded_lines = [line.ljust(max_len) for line in lines]

    transposed = ""
    for col in range(max_len):
        for line in padded_lines:
            transposed += line[col]
        transposed += "\n"

    return transposed[:-1]  # Remove trailing newline character
