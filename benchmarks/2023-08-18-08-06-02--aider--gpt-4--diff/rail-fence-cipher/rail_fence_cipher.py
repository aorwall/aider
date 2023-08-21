def encode(message, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in message:
        fence[rail].append(char)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    return ''.join([''.join(rail) for rail in fence])


def decode(encoded_message, rails):
    fence = [[] for _ in range(rails)]
    rail_lengths = [0] * rails
    rail = 0
    direction = 1

    for _ in encoded_message:
        rail_lengths[rail] += 1
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    i = 0
    for rail in range(rails):
        for _ in range(rail_lengths[rail]):
            fence[rail].append(encoded_message[i])
            i += 1

    result = []
    rail = 0
    direction = 1

    for _ in encoded_message:
        result.append(fence[rail].pop(0))
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    return ''.join(result)
