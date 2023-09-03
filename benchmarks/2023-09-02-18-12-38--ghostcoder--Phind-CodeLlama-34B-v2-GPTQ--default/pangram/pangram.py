import string
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(sentence.lower()))
