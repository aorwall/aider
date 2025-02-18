import math

def cipher_text(plain_text):
    # Normalize the text
    plain_text = plain_text.lower()
    plain_text = ''.join(e for e in plain_text if e.isalnum())

    # Determine dimensions of rectangle
    message_len = len(plain_text)

    if message_len == 0:
        return ""

    num_columns = int(math.sqrt(message_len))
    num_rows = int((message_len / num_columns) + 0.999)  # Always round up

    while num_columns * num_rows < message_len:
        num_columns += 1

    # Pad the message if necessary
    padded_message = plain_text[:num_columns*num_rows]
    while len(padded_message) < num_columns*num_rows:
        padded_message += ' '

    # Create the rectangle
    rectangle = [padded_message[i:i+num_rows] for i in range(0, len(padded_message), num_rows)]

    # Get the ciphered text
    ciphered_text = ''
    for column_index in range(num_columns):
        for row in rectangle:
            try:
                ciphered_text += row[column_index]
            except IndexError:
                break

    return ciphered_text.rstrip()
