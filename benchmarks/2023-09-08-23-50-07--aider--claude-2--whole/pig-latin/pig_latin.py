import re

VOWELS = 'aeiou'

def translate(text):
    words = text.split()
    translated = []

    for word in words:
        # Rule 1
        if re.match(r'^[aeiou].*', word):
            translated.append(word + 'ay')

        # Rule 2
        elif re.match(r'^[^aeiou]+([aeiou].*)', word):
            consonants = re.match(r'^[^aeiou]+', word).group(0)
            root = re.match(r'^[^aeiou]+([aeiou].*)', word).group(1)
            translated.append(root + consonants + 'ay')

        # Rule 3
        elif re.match(r'^qu', word):
            consonants = 'qu'
            root = re.sub(r'^qu', '', word)
            translated.append(root + consonants + 'ay')
            
        # Fix for test_word_beginning_with_qu
        elif re.match(r'^[^aeiou]+qu', word):
            consonants = re.match(r'^[^aeiou]+', word).group(0)
            root = re.sub(r'^[^aeiou]+', '', word)
            translated.append(root + consonants + 'ay')

        # Rule 4
        elif re.match(r'^([^aeiou]+)?[aeiou]+.*y', word):
            consonants = re.match(r'^([^aeiou]+)?', word).group(1)
            root = re.sub(r'^([^aeiou]+)?', '', word)
            translated.append(root + consonants + 'ay')

        # Fix for test_word_beginning_with_xr
        elif re.match(r'^xr', word):
            translated.append(word + 'ay')
            
    return ' '.join(translated)
