import math
import re

def cipher_text(plain_text):
    # Step 1: Normalize the input text
    normalized_text = re.sub(r'\W+', '', plain_text).lower()

    # Check if the normalized text is empty
    if not normalized_text:
        return ''

    # Step 2: Determine the number of rows and columns for the rectangle
    length = len(normalized_text)
    c = math.ceil(math.sqrt(length))
    r = c if c * (c - 1) < length else c - 1

    # Step 3: Organize the normalized text into a rectangle
    rectangle = [normalized_text[i:i+c] for i in range(0, length, c)]

    # Step 4: Read the encoded message by reading down the columns from left to right
    encoded_message = ''.join([''.join([row[j] if j < len(row) else ' ' for row in rectangle]) for j in range(c)])

    # Step 5: Output the encoded text in chunks that fill perfect rectangles, with trailing spaces for short phrases
    return ' '.join([encoded_message[i:i+r] for i in range(0, len(encoded_message), r)])
