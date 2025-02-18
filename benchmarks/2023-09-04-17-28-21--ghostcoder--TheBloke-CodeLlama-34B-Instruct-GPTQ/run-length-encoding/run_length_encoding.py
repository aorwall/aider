import re

def decode(string):
    # Split the input string into a list of substrings using regex
    substrings = re.split('(\d+)', string)

    # Initialize an empty output string
    output = ''

    # Iterate over the substrings
    for substring in substrings:
        # Check if the current substring is a digit
        if substring.isdigit():
            # If it is, convert it to an integer and repeat the previous substring that many times
            output += substring * int(substring)
        else:
            # Otherwise, append the substring to the output without modification
            output += substring

    return output

def encode(string):
    # Initialize an empty output string
    output = ''

    # Get the length of the input string
    length = len(string)

    # Initialize variables to keep track of the current count and the previous character
    count = 0
    prev_char = None

    # Iterate over the characters in the input string
    for char in string:
        # Check if the current character is the same as the previous character
        if char != prev_char:
            # If it isn't, reset the count to 1
            count = 1
        else:
            # Otherwise, increment the count
            count += 1

        # Set the previous character to the current character
        prev_char = char

        # Add the current character and count to the output string
        output += f'{count}{char}'

    return output
