import re

def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        if re.match(r'^(xr|yt|[aeiou])', word):
            translated_word = word + 'ay'
        else:
            match = re.search(r'^(qu|[^aeiou]*qu|[^aeiou]+)(.*)', word)
            if match:
                translated_word = match.group(2) + match.group(1) + 'ay'
            else:
                translated_word = word + 'ay'
        translated_words.append(translated_word)

    return ' '.join(translated_words)