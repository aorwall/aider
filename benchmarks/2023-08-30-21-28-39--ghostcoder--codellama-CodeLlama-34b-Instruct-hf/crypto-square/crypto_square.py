def cipher_text(plain_text):
    # Normalize the input text
    normalized_text = plain_text.lower().replace(" ", "").replace(",", "").replace(".", "")

    # Calculate the number of rows and columns
    num_rows = int(len(normalized_text) ** 0.5)
    num_cols = int(len(normalized_text) / num_rows)

    # Create a list to store the encoded text
    encoded_text = []

    # Loop through each row and column
    for row in range(num_rows):
        for col in range(num_cols):
            # Get the character at the current position
            char = normalized_text[row * num_cols + col]

            # Add the character to the encoded text
            encoded_text.append(char)

    # Return the encoded text
    return "".join(encoded_text)

def crypto_square(plain_text):
    # Call the cipher_text function to get the encoded text
    encoded_text = cipher_text(plain_text)

    # Return the encoded text
    return encoded_text
