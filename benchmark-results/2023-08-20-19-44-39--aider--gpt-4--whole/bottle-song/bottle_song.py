def number_to_word(n):
    words = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten'
    }
    return words[n]

def recite(start, take=1):
    lyrics = []
    for i in range(start, start - take, -1):
        word = number_to_word(i)
        lyrics.append(f"{word} green bottles hanging on the wall,")
        lyrics.append(f"{word} green bottles hanging on the wall,")
        lyrics.append("And if one green bottle should accidentally fall,")
        if i - 1 == 0:
            lyrics.append("There'll be no green bottles hanging on the wall.")
        else:
            word = number_to_word(i - 1)
            lyrics.append(f"There'll be {word.lower()} green bottles hanging on the wall.")
    return '\n'.join(lyrics)
