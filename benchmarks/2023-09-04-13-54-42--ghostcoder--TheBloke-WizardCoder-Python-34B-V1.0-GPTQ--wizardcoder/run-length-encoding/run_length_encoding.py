import re
from itertools import groupby

def decode(string):
    pattern = r'\d+|\D+'
    matches = re.findall(pattern, string)

    if not matches:
        raise ValueError('Invalid input')

    decoded = ''
    for char, count in zip(*([iter(matches)]*2)):
        try:
            decoded += int(count) * char
        except ValueError as e:
            raise ValueError('Invalid input') from e

    return decoded


def encode(string):
    encoded = ''
    for char, group in groupby(string):
        count = len(list(group))
        if count > 1:
            encoded += str(count) + char
        else:
            encoded += char

    return encoded
