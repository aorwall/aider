from itertools import zip_longest

def transpose(input_text):
    lines = input_text.split('\n')
    transposed_lines = [''.join(line) for line in zip_longest(*lines, fillvalue=' ')]
    return '\n'.join(transposed_lines)