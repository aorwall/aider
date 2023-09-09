def commands(binary_str):
    actions = []
    for i, digit in enumerate(binary_str[-5::-1]):
        place = 5-i
        if digit == "1":
            if place == 0:
                actions.append("wink")
            elif place == 1:
                actions.append("double blink") 
            elif place == 2:
                pass
            elif place == 3: 
                actions.append("jump")
            elif place == 4:
                if len(actions) > 0:
                    actions.append("reverse")
    if actions and actions[-1] == "reverse":
        actions = actions[::-1]
    return actions
