def encode(message, rails):
    # Convert string to uppercase and remove spaces
    message = message.upper().replace(' ', '')

    # Create empty matrix to store characters
    matrix = [[None for _ in range(len(message))] for _ in range(rails)]

    # Initialize indices for each row and direction (+1 for right, -1 for left)
    row, step_dir = 0, 1

    # Iterate through message and place character in matrix
    for char in message:
        matrix[row][row] = char

        if ((row == 0 or row == rails - 1) and step_dir != 0) or abs(row + step_dir) >= rails:
            step_dir *= -1

        row += step_dir

    # Read off encoded message from matrix
    encoded_message = ''
    for row in matrix:
        encoded_message += ''.join([char for char in row if char is not None])

    return encoded_message


def decode(encoded_message, rails):
    # Calculate length of each segment
    segment_length = len(encoded_message) // rails
    remaining_chars = len(encoded_message) % rails

    # Create empty matrix to store characters
    matrix = [[None for _ in range(segment_length + (remaining_chars > i))] for i in range(rails)]

    # Place characters in matrix
    current_index = 0
    for row in range(rails):
        for col in range(segment_length + (remaining_chars > row)):
            matrix[row][col] = encoded_message[current_index]
            current_index += 1

    # Initialize indices for each row and direction (+1 for right, -1 for left)
    row, step_dir = 0, 1

    # Read off decoded message from matrix
    decoded_message = []
    while True:
        try:
            decoded_message.append(matrix[row].pop(row))
            if ((row == 0 or row == rails - 1) and step_dir != 0) or abs(row + step_dir) >= rails:
                step_dir *= -1

            row += step_dir
        except IndexError:
            break

    return ''.join(decoded_message)
