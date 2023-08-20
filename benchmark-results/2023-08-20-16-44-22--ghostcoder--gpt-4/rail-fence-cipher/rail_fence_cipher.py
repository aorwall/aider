def encode(message, rails):
    message = message.replace(' ', '')
    rail = [[] for _ in range(rails)]
    num = 0
    down = False

    for char in message:
        rail[num].append(char)
        if num == 0 or num == rails - 1:
            down = not down
        num += 1 if down else -1

    result = []
    for i in rail:
        result += i
    return ''.join(result)


def decode(encoded_message, rails):
    length = len(encoded_message)
    rail = [[] for _ in range(rails)]
    num = 0
    down = False

    for _ in range(length):
        rail[num].append(None)
        if num == 0 or num == rails - 1:
            down = not down
        num += 1 if down else -1

    i = 0
    for r in rail:
        for j in range(len(r)):
            if r[j] == None:
                r[j] = encoded_message[i]
                i += 1

    result = []
    num = 0
    down = False
    for _ in range(length):
        result.append(rail[num].pop(0))
        if num == 0 or num == rails - 1:
            down = not down
        num += 1 if down else -1

    return ''.join(result)