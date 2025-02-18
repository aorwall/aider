import re

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def translate(word):
    if len(word) > 0:
        first_letter = word[0].lower()

        # Rule 1
        if first_letter in VOWELS:
            return f'{word}ay'

        # Rule 2
        elif first_letter in CONSONANTS:
            return f'{word[1:]}{first_letter}ay'

        else:
            return word
    else:
        return word

def translate_sentence(sentence):
    words = sentence.split(' ')
    translated_words = [translate(word) for word in words]
    return ' '.join(translated_words)