import math

def cipher_text(plain_text):
    # Remove whitespace and convert all letters to uppercase
    plain_text = ''.join(plain_text.split()).upper()

    # Calculate the dimensions of the rectangle (rows and columns)
    num_chars = len(plain_text)
    sqrt_num_chars = int(math.ceil(math.sqrt(num_chars)))
    cols = sqrt_num_chars
    rows = sqrt_num_chars

    # Create the matrix
    matrix = []
    for i in range(rows):
        matrix.append([''] * cols)

    for i in range(len(plain_text)):
        matrix[i//cols][i%cols] = plain_text[i]

    # Read down the columns and join them together to form the encrypted string
    encrypted_text = ''
    for col in range(cols):
        encrypted_text += ''.join([matrix[row][col] for row in range(rows)])
        encrypted_text += ' '
    return encrypted_text[:-1]
