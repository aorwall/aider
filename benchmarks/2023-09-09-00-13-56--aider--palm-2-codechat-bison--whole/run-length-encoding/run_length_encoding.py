def decode(string):
    """
    Decodes a run-length encoded string.

    Args:
        string: The run-length encoded string.

    Returns:
        The decoded string.
    """

    result = ""
    count = 1
    for character in string:
        if character.isdigit():
            count = int(character)
        elif count > 0:
            result += character * count
            count = 1
        else:
            result += character

    return result


def encode(string):
    """
    Encodes a string using run-length encoding.

    Args:
        string: The string to encode.

    Returns:
        The run-length encoded string.
    """

    result = ""
    count = 1
    for character in string:
        if character == result[-1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += character
            count = 1

    if count > 1:
        result += str(count)

    return result
