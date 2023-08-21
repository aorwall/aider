def encode(message, rails):
    rails_list = [''] * rails
    rail, step = 0, 1

    for char in message:
        rails_list[rail] += char
        if rail == 0:
            step = 1
        elif rail == rails - 1:
            step = -1
        rail += step

    return ''.join(rails_list)


def decode(encoded_message, rails):
    rails_list = [''] * rails
    rail_lengths = [0] * rails
    rail, step = 0, 1

    for _ in encoded_message:
        rail_lengths[rail] += 1
        if rail == 0:
            step = 1
        elif rail == rails - 1:
            step = -1
        rail += step

    i = 0
    for rail in range(rails):
        for _ in range(rail_lengths[rail]):
            rails_list[rail] += encoded_message[i]
            i += 1

    rail, step = 0, 1
    decoded_message = ''
    for _ in encoded_message:
        decoded_message += rails_list[rail][0]
        rails_list[rail] = rails_list[rail][1:]
        if rail == 0:
            step = 1
        elif rail == rails - 1:
            step = -1
        rail += step

    return decoded_message
