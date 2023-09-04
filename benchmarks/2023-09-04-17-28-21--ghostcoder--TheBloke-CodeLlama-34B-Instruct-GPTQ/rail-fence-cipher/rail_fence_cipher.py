def encode(message, rails):
    # Initialize empty matrix to store the encoded message
    encoded_matrix = [[None] * len(message) for _ in range(rails)]

    # Loop through each character in the message
    for i, char in enumerate(message):
        # Calculate the row index based on the current iteration number
        row_index = i % rails

        # Add the character to the corresponding position in the matrix
        encoded_matrix[row_index][i] = char

    # Flatten the matrix into a single string
    encoded_string = ''.join([char for row in encoded_matrix for char in row if char is not None])

    return encoded_string


def decode(encoded_message, rails):
    # Initialize empty list to store the decoded characters
    decoded_chars = []

    # Loop through each character in the encoded message
    for i, char in enumerate(encoded_message):
        # Calculate the row index based on the current iteration number
        row_index = i % rails

        # Get the column index based on the row index and the total number of columns
        col_index = int((len(encoded_message) / rails) - ((i // rails) + 1))

        # Append the character at the calculated position in the matrix to the decoded chars list
        decoded_chars.append(encoded_message[col_index][row_index])

    # Join the decoded chars list into a single string
    decoded_string = ''.join(decoded_chars)

    return decoded_string
