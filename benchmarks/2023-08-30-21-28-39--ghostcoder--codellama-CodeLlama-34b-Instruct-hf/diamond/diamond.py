def rows(letter):
    return [(letter.upper() + i * ' ' + letter.upper()).center(len(letter) * 2 + 1) for i in range(len(letter))]
