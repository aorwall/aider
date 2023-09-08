def encode(message, rails):
    if rails == 1:
        return message

    fence = [''] * rails
    index, step = 0, 1

    for char in message:
        fence[index] += char

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1
        index += step

    encoded_message = ''
    for row in fence:
        encoded_message += row

    return encoded_message

def decode(encoded_message, rails):
    fence = [''] * rails
    index, step = 0, 1

    for char in encoded_message:
        fence[index] += char

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1
        index += step

    message = ''
    for row in fence:
        message += row

    return message
