def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    handshake = [action for digit, action in zip(binary_str[::-1], actions) if digit == '1']
    if len(binary_str) == 5 and binary_str[0] == '1':
        handshake.reverse()
    return handshake
