def decode(string):
    result = ""
    number = ""
    for char in string:
        if char.isdigit():
            number += char
        else:
            result += char * int(number) if number else char
            number = ""
    return result


def encode(string):
    result = ""
    current_char = None
    counter = 0

    for char in string:
        if char != current_char:
            if current_char is not None:
                result += str(counter) + current_char
            current_char = char
            counter = 1
        else:
            counter += 1

    if current_char is not None:
        result += str(counter) + current_char

    return result.strip()
