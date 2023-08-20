def commands(binary_str):
    actions = []
    binary_str = binary_str[::-1]  # Reverse the binary string
    if len(binary_str) >= 1 and binary_str[0] == '1':
        actions.append("wink")
    if len(binary_str) >= 2 and binary_str[1] == '1':
        actions.append("double blink")
    if len(binary_str) >= 3 and binary_str[2] == '1':
        actions.append("close your eyes")
    if len(binary_str) >= 4 and binary_str[3] == '1':
        actions.append("jump")
    if len(binary_str) >= 5 and binary_str[4] == '1':
        actions.reverse()
    return actions
