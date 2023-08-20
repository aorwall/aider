def transpose(lines):
    lines = lines.split('\n')
    max_length = max(len(line) for line in lines)
    transposed = [[' ']*len(lines) for _ in range(max_length)]
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            transposed[j][i] = char
    return '\n'.join(''.join(row).rstrip() for row in transposed)
