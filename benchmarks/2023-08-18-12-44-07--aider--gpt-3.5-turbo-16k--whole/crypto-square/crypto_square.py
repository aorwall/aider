def cipher_text(plain_text):
    # Normalize the text by removing spaces and punctuation, and converting to lowercase
    normalized_text = ''.join(char.lower() for char in plain_text if char.isalnum())

    # Determine the number of rows and columns for the rectangle
    length = len(normalized_text)
    rows = int(length ** 0.5)
    columns = rows if rows * rows >= length else rows + 1

    # Pad the normalized text with spaces to form a rectangle
    normalized_text += ' ' * (rows * columns - length)

    # Encode the text by reading down the columns
    encoded_text = ''
    for col in range(columns):
        for row in range(rows):
            encoded_text += normalized_text[row * columns + col]

        # Add a space after each chunk of encoded text, except for the last chunk
        if col < columns - 1:
            encoded_text += ' '

    return encoded_text
