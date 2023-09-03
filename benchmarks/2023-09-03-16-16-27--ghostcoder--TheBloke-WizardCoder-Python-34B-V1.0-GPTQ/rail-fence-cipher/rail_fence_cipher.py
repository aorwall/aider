def encode(message, rails):
    if rails == 0 or rails >= len(message):
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
    if rails == 0 or rails >= len(encoded_message):
        return encoded_message

    fence = [''] * rails
    index, step = 0, 1

    for i in range(len(encoded_message)):
        fence[index] += '_'
        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1
        index += step

    rows = len(fence)
    cols = len(encoded_message) // rows + len(encoded_message) % rows

    decoded_message = []
    for j in range(cols):
        for i in range(rows):
            try:
                decoded_message.append(fence[i][j])
            except IndexError:
                continue

    return ''.join(decoded_message[:len(encoded_message)]).replace('_', '')
