def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        if len(word) > 1 and word[0] == 'xr':
            translated_words.append(f'{word[1:]}{word[0]}ay')

        elif len(word) > 1 and word[0] == 'yt':
            translated_words.append(f'{word[1:]}{word[0]}ay')

        elif len(word) > 2 and word[:2] == 'qu':
            translated_words.append(f'{word[2:]}{word[:2]}ay')

        elif len(word) > 1 and word[1] == 'y':
            translated_words.append(f'{word[2:]}{word[:2]}ay')

        elif word[0] in ['a', 'e', 'i', 'o', 'u']:
            translated_words.append(f'{word}ay')

        else:
            translated_words.append(f'{word[len(word)-1:]}{word[:-1]}ay')

    return ' '.join(translated_words)
