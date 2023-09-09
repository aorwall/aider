import string

def rotate(text, key):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    shifted = alphabet[key:] + alphabet[:key] 
    table = str.maketrans(alphabet, shifted)
    return text.translate(table)
