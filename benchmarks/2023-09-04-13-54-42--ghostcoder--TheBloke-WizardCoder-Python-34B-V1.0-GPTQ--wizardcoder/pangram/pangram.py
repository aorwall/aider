import string

def is_pangram(sentence):
    # Convert all characters to lowercase
    sentence = sentence.lower()

    # Remove spaces and punctuation marks
    sentence = ''.join([c for c in sentence if c not in string.whitespace and c not in string.punctuation])

    # Check if all letters are present in the sentence
    return set(string.ascii_lowercase) <= set(sentence)
