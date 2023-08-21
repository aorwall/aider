import re

def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        if re.match('^(xr|yt|[aeiou])', word):
            # Rule 1: word begins with a vowel sound
            translated_word = word + 'ay'
        elif re.match('^(qu|[^aeiou]+qu)', word):
            # Rule 3: word starts with a consonant sound followed by "qu"
            match = re.match('^(qu|[^aeiou]+qu)', word)
            translated_word = word[match.end():] + match.group() + 'ay'
        elif re.match('^[^aeiouy]+', word):
            # Rule 2: word begins with a consonant sound
            match = re.match('^[^aeiouy]+', word)
            translated_word = word[match.end():] + match.group() + 'ay'
        else:
            # Rule 4: word contains a "y" after a consonant cluster or as the second letter in a two letter word
            match = re.match('^[^aeiou]*y', word)
            translated_word = word[match.end():] + match.group() + 'ay'

        translated_words.append(translated_word)

    return ' '.join(translated_words)
