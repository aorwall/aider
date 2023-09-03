def decode(string):
    pass


def encode(string):
    """Encode a string using run-length encoding."""
    if not string:
        return ""

    # Initialize variables
    prev_char = ''
    count = 1
    result = []

    # Iterate over the input string
    for char in string:
        # If current character is same as previous character, increment counter
        if char == prev_char:
            count += 1
        else:
            # Append the previous character and its count to the result list
            if prev_char:
                result.append("{}".format(prev_char + str(count)) * (count // 2))
            # Set new previous character and reset count to 1
            prev_char = char
            count = 1

    # Append last character and its count to the result list
    result.append("{}".format(prev_char + str(count)) * (count // 2))

    return ''.join(result)



def decode(encoded_str):
    """Decode a string previously encoded with run-length encoding."""
    if not encoded_str:
        return ""

    # Initialize variables
    i = 0
    decoded_str = []

    while i < len(encoded_str):
        # Extract count and character from the next two positions in the string
        count = int(encoded_str[i])
        char = encoded_str[i+1]

        # Repeat the character count number of times and append to result
        decoded_str.extend([char] * count)

        # Move to the next pair of characters in the string
        i += 2

    return ''.join(decoded_str)



def decode(string):
    """Decode a string previously encoded with run-length encoding."""
    if len(string) == 0:
        return ""

    # Initialize variables
    index = 0
    result = []

    while index < len(string):
        # Extract count and character from the next two positions in the string
        count = int(string[index])
        char = string[index+1]

        # Repeat the character count number of times and append to result
        for _ in range(count):
            result.append(char)

        # Move to the next pair of characters in the string
        index += 2

    return ''.join(result)
