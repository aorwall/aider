def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    result = [actions[i] for i in range(4) if binary_str.zfill(5)[::-1][i] == '1']
    if binary_str.zfill(5)[::-1][4] == '1':
        result.reverse()
    return result