def cipher_text(plain_text):
    # Normalize the input text
    normalized_text = plain_text.lower()
    normalized_text = ''.join([char for char in normalized_text if char.isalpha()])

    # Calculate the dimensions of the rectangle
    num_columns = int(len(normalized_text) ** 0.5)
    num_rows = len(normalized_text) // num_columns

    # Pad the remaining cells with spaces
    padded_text = normalized_text[:num_columns * num_rows]
    padded_text += ' ' * (num_columns * num_rows - len(padded_text))

    # Create the matrix
    matrix = [padded_text[i:i+num_columns] for i in range(0, len(padded_text), num_columns)]

    # Read down the columns going left to right
    ciphered_text = ''
    for col in zip(*matrix):
        ciphered_text += ''.join(col) + ' '

    return ciphered_text.strip()
