import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence = sentence.lower()

    # Remove spaces because we only care about alphabetic characters
    sentence = sentence.translate({ord(' '): None})

    return alphabet.issubset(set(sentence))
