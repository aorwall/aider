def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence = set(sentence.lower())
    return alphabet.issubset(sentence)
