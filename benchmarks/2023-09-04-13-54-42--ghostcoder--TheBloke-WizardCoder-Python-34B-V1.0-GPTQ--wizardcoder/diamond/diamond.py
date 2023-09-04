from string import ascii_uppercase

def rows(letter):
    if len(letter) != 1 or not letter.isalpha() or not letter.isascii():
        raise ValueError("Invalid input")

    letter = letter.upper()
    alphabet = list(ascii_uppercase)
    index = alphabet.index(letter)
    height = index * 2 + 1
    diameter = height - 1
    output = []

    for i in range(height):
        row = ""

        # Add left padding
        for j in range((diameter - i) // 2):
            row += " "

        # Add middle character(s)
        if i == 0 or i == height - 1:
            row += letter
        else:
            row += alphabet[abs(i - index)] + alphabet[index - abs(i - index)]

        # Add right padding
        for j in range((diameter - i) // 2):
            row += " "

        output.append(row)

    return output
