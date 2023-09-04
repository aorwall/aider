import re

def decode(rle_string):
    pattern = r'(\d+)?([\w\s])?'
    return ''.join([match.group(2)*int(match.group(1)) if match.group(1) and match.group(2) else match.group(0) for match in re.finditer(pattern, rle_string)])

def encode(original_string):
    encoded_string = ""
    current_char = original_string[0]
    counter = 1

    for char in original_string[1:]:
        if char == current_char:
            counter += 1
        else:
            encoded_string += str(counter) + current_char
            current_char = char
            counter = 1

    encoded_string += str(counter) + current_char
    return encoded_string