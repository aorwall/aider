def cipher_text(plain_text):
    # Normalize the input text
    plain_text = plain_text.lower().replace(" ", "").replace(",", "").replace(".", "")

    # Calculate the dimensions of the square
    length = len(plain_text)
    rows = int(length ** 0.5) + (1 if length % int(length ** 0.5) else 0)
    columns = int(length / rows) + (1 if length % rows else 0)

    # Create the square
    square = [plain_text[i:i + columns] for i in range(0, length, columns)]

    # Read down the columns to get the encoded text
    encoded_text = ""
    for i in range(columns):
        for j in range(rows):
            if i < columns - 1 or j < rows - 1:
                encoded_text += square[j][i]
            else:
                encoded_text += square[j][i] + " "

    # Remove trailing spaces and return the encoded text
    return encoded_text.rstrip()
