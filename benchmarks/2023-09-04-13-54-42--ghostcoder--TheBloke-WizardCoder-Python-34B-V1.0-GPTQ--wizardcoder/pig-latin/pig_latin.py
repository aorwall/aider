import re

VOWELS = set('aeiou')
CONSONANTS = set('bcdfghjklmnpqrstvwxyz')

def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        if not VOWELS & set(word[:1].lower()) and len(word) > 1:
            if 'qu' == word[:2].lower():
                word = word[2:] + word[:2]
            else:
                word = word[1:] + word[0]

        if not VOWELS & set(word[:1].lower()):
            word += 'ay'

        translated_words.append(word)

    return ' '.join(translated_words)
