import math
def encode(message, rails):
    """Encode a message using the Rail Fence cipher with given number of rails."""
    if rails == 1:
        return message

    fence = [''] * rails
    index, step = 0, 1
    for char in message:
        fence[index] += char

        # Move up/down the rail
        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    encoded_message = ''.join([rail for rail in fence])
    return encoded_message


def decode(encoded_message, rails):
    """Decode an encoded message using the Rail Fence cipher with given number of rails."""
    if rails == 1:
        return encoded_message

    fence = [''] * rails
    row, step = 0, 1
    for i in range(len(encoded_message)):
        fence[row] += '_'
        row += step

        # Change direction when reaching top or bottom rail
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1

    # Remove underscores and fill in characters from encoded message
    for i, char in enumerate(encoded_message):
        fence[i % (rails-1)] += char

    # Read off the rows to get the original message
    decoded_message = ''
    for rail in fence:
        decoded_message += rail.replace('_', '')

    return decoded_message
