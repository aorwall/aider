def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(letter)

    top_half = list(map(chr, range(65, 65+index)))[::-1]
    bottom_half = list(map(chr, range(65+index, 74)))

    lines = []
    max_width = len(" ".join(top_half))

    for i in range(len(top_half)):
        line = "".join((top_half[i], ) + tuple(' ' * (max_width - 2*len(top_half[i]))))
        if i < len(bottom_half):
            line += bottom_half[i]
        lines.append(line)

    return "\n".join(lines)
