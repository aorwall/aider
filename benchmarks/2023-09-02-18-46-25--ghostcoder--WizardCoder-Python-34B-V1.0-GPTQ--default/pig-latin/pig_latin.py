def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']

    def is_vowel(word):
        if len(word) == 0:
            return False
        elif word[0] in vowels:
            return True
        else:
            return False

    words = text.split()
    new_words = []

    for word in words:
        if is_vowel(word):
            new_word = word + 'ay'
        elif word[:2].lower() in ['bl', 'br', 'gl', 'gr', 'pl', 'pr', 'cl', 'cr', 'fl', 'fr', 'dr', 'tr', 'ch', 'sh', 'th', 'sw', 'sc', 'squ', 'qu'] and not (len(word) > 2 and word[1] == 'u'):
            new_word = word[2:] + word[:2] + 'ay'
        elif word[0] == 'y':
            new_word = word[1:] + word[0] + 'ay'
        elif word[0] == 'xr':
            new_word = word[1:] + 'ray'
        elif word[0] == 'yt':
            new_word = word[1:] + 'yta'
        else:
            new_word = word[1:] + word[0] + 'ay'

        new_words.append(new_word)

    return ' '.join(new_words)
