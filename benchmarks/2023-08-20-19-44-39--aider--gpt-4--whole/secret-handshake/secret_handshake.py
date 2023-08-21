def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    handshake = [action for i, action in enumerate(actions) if binary_str.zfill(5)[::-1][i] == '1']
    if binary_str.zfill(5)[0] == '1':
        handshake.reverse()
    return handshake
