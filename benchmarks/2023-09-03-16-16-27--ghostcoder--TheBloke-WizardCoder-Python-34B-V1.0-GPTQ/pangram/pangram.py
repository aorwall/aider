import string

alphabet = set(string.ascii_lowercase)

def is_pangram(sentence):
    seen_letters = set()
    for char in sentence.lower():
        if char.isalpha() and char not in seen_letters:
            seen_letters.add(char)

    return len(seen_letters) == len(alphabet)
