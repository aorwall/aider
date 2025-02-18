def encode(message, rails):
    rows = [''] * rails
    for i in range(len(message)):
        index = i % rails
        rows[index] += message[i]

    return ''.join(rows)


def decode(encoded_message, rails):
    length = len(encoded_message)
    message_length = (length + rails - 1) // rails
    rows = ['' for _ in range(rails)]
    output = [''] * message_length

    for col in range(message_length):
        for row in range(rails):
            if col < rails and row >= col or col >= rails and row + col < length:
                index = col + row * message_length
                char = encoded_message[index]
                output[col] += char

    return ''.join(output)
