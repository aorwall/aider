import string

def is_pangram(sentence):
    letters = set(sentence.lower())
    return set(string.ascii_lowercase) <= letters
