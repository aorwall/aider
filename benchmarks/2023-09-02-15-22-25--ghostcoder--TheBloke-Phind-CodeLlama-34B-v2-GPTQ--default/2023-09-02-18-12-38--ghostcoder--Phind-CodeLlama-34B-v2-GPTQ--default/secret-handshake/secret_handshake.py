def commands(binary_str):
    # Define the actions based on the binary digits
    actions = {
        '0': 'wink',
        '1': 'double blink',
        '2': 'close your eyes',
        '3': 'jump',
        '4': 'reverse order'
    }

    # Convert the binary string into a list of actions
    result = []
    for digit in binary_str:
        action = actions[digit]

        if action == 'reverse order':
            result = result[::-1]
        else:
            result.append(action)

    return result
