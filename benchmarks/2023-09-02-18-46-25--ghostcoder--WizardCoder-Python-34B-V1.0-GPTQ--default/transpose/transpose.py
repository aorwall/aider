def transpose(text):
    lines = text.split('\n')
    max_length = len(max(lines, key=len) if lines else '')

    for i in range(len(lines)):
        lines[i] += ' ' * (max_length - len(lines[i]))

    return '\n'.join([''.join([line[j] for j in range(max_length)] for line in lines])
                   )  # Added closing parenthesis to the return statement