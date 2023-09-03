import re

VOWELS = 'aeiouAEIOU'
CONSONANTS = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

def translate(text):
    words = text.split()
    translated = []

    for word in words:
        if len(word) == 0:
            continue # skip empty strings
        elif word[0] in VOWELS:
            translated.append(word + 'ay')
        elif word[:2].lower() == 'qu':
            translated.append(word[2:] + word[:2] + 'ay')
        else:
            match = re.match('[' + CONSONANTS + ']+|xr|yt', word)
            if match:
                prefix = match.group()
                suffix = word[len(prefix):]
                translated.append(suffix + prefix + 'ay')
            else:
                raise ValueError("Invalid input")

    return ' '.join(translated)
