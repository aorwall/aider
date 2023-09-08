def commands(binary_str):
    actions = {
        "1": "wink",
        "10": "double blink",
        "100": "close your eyes",
        "1000": "jump",
        "10000": "Reverse the order of the operations in the secret handshake."
    }

    binary_str = binary_str.lstrip('0')
    if not binary_str:
        binary_str = '0'

    binary_int = int(binary_str, 2)
    code = []

    for i in range(5):
        if binary_int & 1:
            code.append(actions[str(1 << i)])
        binary_int >>= 1

    if 'Reverse the order of the operations in the secret handshake.' in code:
        code.remove('Reverse the order of the operations in the secret handshake.')
        code = code[::-1]

    return code
