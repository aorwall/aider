def transpose(lines):
    rows = []
    max_length = max(map(len, line) for line in lines if line)
    for i in range(max_length):
        rows.append([])
    for line in lines:
        line_length = len(line)
        for i, char in enumerate(line):
            if i < line_length:
                rows[i].append(char)
        for i in range(line_length, max_length):
            rows[i].append(' ')
    return ['\n'.join(row) for row in rows]
