def transpose(lines):
    # Split lines into list of strings
    lines = [list(line) for line in lines]

    # Find max length for padding
    max_len = max([len(l) for l in lines])

    # Transpose lines into columns
    cols = [[[] for _ in range(max_len)] for _ in range(len(lines))]
    for col_idx in range(max_len):
        for line in reversed(lines):
            try:
                cols[col_idx].append(str(line[col_idx]))
            except IndexError:
                cols[col_idx].append(' ')

    # Join columns back into lines
    transposed_lines = [''.join(col).rstrip() for col in zip(*cols)]

    return transposed_lines
