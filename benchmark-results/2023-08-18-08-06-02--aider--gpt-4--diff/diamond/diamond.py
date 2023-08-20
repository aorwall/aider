def rows(letter):
    letters = [chr(i) for i in range(ord('A'), ord(letter) + 1)]
    diamond = []
    for i, letter in enumerate(letters):
        outer_spaces = ' ' * (len(letters) - i - 1)
        if letter == 'A':
            diamond.append(outer_spaces + letter + outer_spaces)
        else:
            inner_spaces = ' ' * (2 * i - 1)
            diamond.append(outer_spaces + letter + inner_spaces + letter + outer_spaces)
    diamond += diamond[:-1][::-1]
    return diamond
