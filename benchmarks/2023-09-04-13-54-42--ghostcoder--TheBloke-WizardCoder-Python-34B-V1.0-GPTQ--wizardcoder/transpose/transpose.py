def transpose(lines):
    if not lines:
        raise ValueError("Empty input")

    max_len = len(max(lines, key=lambda x: len(x)))

    padded_lines = []
    for line in lines:
        padding = " " * (max_len - len(line))
        padded_lines.append(padding + line)

    transposed_rows = ["".join([padded_lines[j][i] for j in range(len(padded_lines))]) for i in range(max_len)]
    return "\n".join(transposed_rows)
