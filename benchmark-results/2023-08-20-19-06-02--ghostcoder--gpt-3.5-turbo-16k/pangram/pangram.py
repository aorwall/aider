def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for char in alphabet:
        if char not in sentence:
            return False
    return True