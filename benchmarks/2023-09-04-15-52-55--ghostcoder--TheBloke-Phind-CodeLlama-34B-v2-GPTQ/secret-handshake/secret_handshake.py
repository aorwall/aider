def commands(binary_str):
    actions = {
        0: 'wink',
        1: 'double blink',
        2: 'close your eyes',
        3: 'jump',
        4: None, # reverse actions
    }

    cmds = []
    reversed_cmds = False

    for idx in range(len(binary_str) - 1, -1, -1):
        bit = int(binary_str[idx])

        if bit == 4:
            cmds = cmds[::-1]
            reversed_cmds = True
            break

        if not reversed_cmds and bit != 4:
            cmd = actions[bit]
            if cmd:
                cmds.append(cmd)

    return cmds
