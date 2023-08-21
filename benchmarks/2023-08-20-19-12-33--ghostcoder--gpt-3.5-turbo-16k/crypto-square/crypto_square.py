import math

def cipher_text(plain_text):
    # Normalize the text
    normalized_text = plain_text.lower().replace(" ", "").replace(",", "").replace(".", "")

    # Calculate the number of rows and columns
    length = len(normalized_text)
    rows = math.isqrt(length)
    columns = rows if rows * rows == length else rows + 1

    # Create the square code
    square_code = ""
    for i in range(columns):
        for j in range(i, length, columns):
            square_code += normalized_text[j]
        square_code += " "

    # Pad the last chunk with trailing spaces if needed
    last_chunk_length = len(square_code.split()[-1])
    if last_chunk_length < rows:
        square_code += " " * (rows - last_chunk_length)

    return square_code.strip()