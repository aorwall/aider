import string

def rotate(text, key):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    rotated_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, rotated_alphabet)
    return text.translate(table)
