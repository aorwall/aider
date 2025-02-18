def commands(binary_string):
    # Convert the input binary string to a list of integers
    binary_list = [int(x) for x in binary_string]

    # Initialize an empty list to store the actions
    actions = []

    # Iterate over the binary list, starting from the end
    for i in range(len(binary_list)-1, -1, -1):
        # If the current element is 1, add the corresponding action to the list
        if binary_list[i] == 1:
            if i == 0:
                actions.append('wink')
            elif i == 1:
                actions.append('double blink')
            elif i == 2:
                actions.append('close your eyes')
            elif i == 3:
                actions.append('jump')

    # Check if the reversal flag is set
    if len(actions) > 0 and actions[-1] == 'Reverse':
        # Remove the reversal flag
        actions.pop()

        # Reverse the list of actions
        actions.reverse()

    return actions