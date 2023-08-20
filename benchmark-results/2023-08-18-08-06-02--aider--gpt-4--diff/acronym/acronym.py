def abbreviate(words):
    words = words.replace('-', ' ').replace('_', ' ').split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym
