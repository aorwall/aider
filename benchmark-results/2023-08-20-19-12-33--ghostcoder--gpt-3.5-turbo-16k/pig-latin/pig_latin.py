def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    pig_latin_words = []
    for word in words:
        if word[0] in vowels or word[:2] in ['xr', 'yt']:
            pig_latin_words.append(word + 'ay')
        elif word[:2] == 'qu':
            pig_latin_words.append(word[2:] + 'quay')
        else:
            consonant_cluster = ''
            i = 0
            while i < len(word) and word[i] not in vowels:
                if i < len(word) - 1 and word[i] == 'y' and word[i+1] not in vowels:
                    break
                consonant_cluster += word[i]
                i += 1
            pig_latin_words.append(word[i+1:] + consonant_cluster + 'ay')
    return ' '.join(pig_latin_words)