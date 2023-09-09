def rows(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    width = 2 * (alphabet.index(letter) + 1) - 1
    
    rows = []
    for i in range(width):
        if i == 0 or i == width - 1:
            rows.append(' ' * (width - 1) + alphabet[0])
        else:
            letter1 = alphabet[width//2 - min(i, width-i-1)]
            letter2 = letter1
            row = ' ' * (width//2 - min(i, width-i)) + letter1 + ' ' * (width - 2*min(i, width-i) - 2) + letter2
            rows.append(row)
    
    return rows
