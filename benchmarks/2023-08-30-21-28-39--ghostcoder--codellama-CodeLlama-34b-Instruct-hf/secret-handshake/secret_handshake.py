def commands(binary_str):
    actions = []
    for i in range(len(binary_str)):
        if binary_str[i] == "1":
            actions.append(["wink", "double blink", "close your eyes", "jump"][i % len(actions)])
    if "10000" in binary_str:
        actions.reverse()
    return actions