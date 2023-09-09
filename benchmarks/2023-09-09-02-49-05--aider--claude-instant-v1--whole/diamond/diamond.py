def rows(letter):
    letter = letter.upper()
    height = width = 1 + ord(letter) - ord('A')
    result = []
    for i in range(height):
        row = ""
        for j in range(width):
            if i == 0 or i == height-1 or j == i or j == width-i-1:
                row += letter
            else:
                row += " "
        result.append(row)
    return result
