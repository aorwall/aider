import math

def cipher_text(plain_text):
    # Step 1: Normalize the input text
    normalized_text = ''.join(c for c in plain_text.lower() if c.isalnum())

    # If the normalized text is empty, return an empty string
    if not normalized_text:
        return ''

    # Step 2: Determine the number of rows and columns for the rectangle
    c = math.ceil(math.sqrt(len(normalized_text)))
    r = c if c * (c - 1) >= len(normalized_text) else c

    # Step 3: Organize the normalized text into a rectangle
    rectangle = [normalized_text[i:i+c] for i in range(0, len(normalized_text), c)]

    # Step 4: Read the encoded message by reading down the columns from left to right
    encoded_message = ''.join(''.join(row[j] for row in rectangle if j < len(row)) for j in range(c))

    # Step 5: Output the encoded text in chunks that fill perfect rectangles
    # Pad each chunk with trailing spaces to make it of length r
    return ' '.join(encoded_message[i:i+r].ljust(r) for i in range(0, len(encoded_message), r))