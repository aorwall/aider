def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(letter)

    lines = []
    for i in range(index + 1):
        line = ""
        for j in range(index - i):
            line += "·"
        line += alphabet[i]
        for j in range(index - i):
            line += "·"
        lines.append(line)

    for i in reversed(range(len(lines))):
        lines[i] = lines[i].center((2 * len(alphabet[i])) + len(lines[i]) % 2, " ")

    return "\n".join(reversed(lines[:-1]) + [lines[-1]] + lines[1:-1])
