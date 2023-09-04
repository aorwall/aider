import re
from collections import Counter

def is_isogram(string):
    string = string.lower()
    string = re.sub('[^a-z0-9]+', '', string)

    char_count = Counter(string)

    for count in char_count.values():
        if count > 1:
            return False

    return True
