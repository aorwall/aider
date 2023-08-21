import re

def abbreviate(words):
    words = re.sub(r'[^a-zA-Z0-9- ]', '', words)  # remove all punctuation except hyphens
    words = re.split(r'[- ]', words)  # split words by spaces and hyphens
    acronym = ''.join(word[0].upper() for word in words if word)  # take the first letter of each word, convert to uppercase and join
    return acronym
