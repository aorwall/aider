def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    result = []

    for word in words:
        if word[0] in vowels or word[:2] in ['xr', 'yt']:
            result.append(word + 'ay')
        elif word[0] == 'y':
            result.append(word[1:] + word[0] + 'ay')
        else:
            if 'qu' in word:
                idx = word.index('qu') + 2
            elif 'y' in word:
                idx = word.index('y')
            else:
                idx = min([i for i, letter in enumerate(word) if letter in vowels])
            result.append(word[idx:] + word[:idx] + 'ay')

    return ' '.join(result)
