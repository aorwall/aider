def transpose(input_text):
    if not input_text:
        return ""

    lines = input_text.split('\n')
    max_length = max(len(line) for line in lines)

    # Pad lines to the left with spaces
    lines = [line.ljust(max_length) for line in lines]

    # Transpose lines
    transposed = [''.join(line[i] for line in lines if i < len(line)).rstrip() for i in range(max_length)]

    return '\n'.join(transposed)
