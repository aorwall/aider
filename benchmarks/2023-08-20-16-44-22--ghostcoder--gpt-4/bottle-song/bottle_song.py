def recite(start, take=1):
    num_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                   6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
    lyrics = []
    for i in range(start, 0, -take):
        word_i = num_to_word[i].capitalize() if i == start else num_to_word[i]
        word_take = num_to_word[take]
        word_remaining = 'no' if i-take == 0 else num_to_word[i-take]
        lyrics.append(f"{word_i} green bottle{'s' if i > 1 else ''} hanging on the wall,")
        lyrics.append(f"{word_i} green bottle{'s' if i > 1 else ''} hanging on the wall,")
        lyrics.append(f"And if {word_take} green bottle{'s' if take > 1 else ''} should accidentally fall,")
        lyrics.append(f"There'll be {word_remaining} green bottle{'s' if i-take > 1 else ' no' if i-take == 0 else ''} hanging on the wall.")
    return lyrics