import re

def abbreviate(words):
    words = words.upper()
    words = re.sub(r'[^\w-]', ' ', words)
    acronym = ''
    for word in words.split('-'):
        acronym += word[0]
    return acronym
