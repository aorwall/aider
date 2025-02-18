def encode(message, rails):
    if rails == 1:
        return message

    rail_fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in message:
        rail_fence[rail].append(char)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    encoded_message = ''.join([''.join(rail) for rail in rail_fence])
    return encoded_message


def decode(encoded_message, rails):
    if rails == 1:
        return encoded_message

    rail_fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in encoded_message:
        rail_fence[rail].append(None)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    index = 0
    for rail in rail_fence:
        for i in range(len(rail)):
            rail[i] = encoded_message[index]
            index += 1

    rail = 0
    direction = 1
    decoded_message = ''

    for _ in range(len(encoded_message)):
        decoded_message += rail_fence[rail].pop(0)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return decoded_message