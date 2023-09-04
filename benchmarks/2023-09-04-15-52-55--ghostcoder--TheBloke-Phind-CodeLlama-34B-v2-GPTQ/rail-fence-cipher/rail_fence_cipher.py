def encode(message, rails):
    # Create the matrix to fit the message
    matrix = [[''] * (len(message) // rails + 1) for _ in range(rails)]

    # Define the movement direction
    down = False
    row = 0
    column = 0

    # Start filling the matrix
    for char in message:
        matrix[row][column] = char

        if row == 0 or row == rails - 1:
            down = not down

        if down:
            row += 1
        else:
            row -= 1
            column += 1

    # Combine the characters in each row into a string
    encoded_message = ''.join([''.join(row) for row in matrix])

    return encoded_message[:len(message)]


def decode(encoded_message, rails):
    # Calculate the size of the matrix
    size = len(encoded_message)
    columns = int((size + rails - 1) / rails)
    rows = rails

    # Fill the matrix with the encoded characters
    matrix = [list('.' * columns) for _ in range(rows)]

    index = 0
    for r in range(rows):
        c = 0
        while index < len(encoded_message) and c < columns:
            matrix[r][c] = encoded_message[index]
            index += 1
            c += 1

    # Read the message from the matrix following the zig-zag path
    column = 0
    row = 0
    decoded_message = ''

    while True:
        try:
            decoded_message += matrix[row][column]
        except IndexError:
            break

        if row == 0 or row == rails - 1:
            column += 1
            if row == 0:
                row += 1
            elif row == rails - 1:
                row -= 1
        else:
            if row < rails // 2:
                row += 1
            else:
                row -= 1

    return decoded_message
