def recite(start_verse=1, end_verse=12):
    verses = [
        "the house that Jack built.",
        "malt",
        "rat",
        "cat",
        "dog",
        "cow with the crumpled horn",
        "maiden all forlorn",
        "man all tattered and torn",
        "priest all shaven and shorn",
        "rooster that crowed in the morn",
        "farmer sowing his corn",
        "horse and the hound and the horn"
    ]

    rhyme = []
    for i in range(start_verse-1, end_verse):
        verse = f"This is {verses[i]}" if i == 0 else f"that {verses[i]} {verses[i-1]}"
        if i > 0:
            verse += ''.join([f" that {'lay' if j < i-1 else 'laid'} in " if j%3==0 else '' for j in range(i)][::-1])
        rhyme.append(verse + ('' if i<end_verse-1 else '.'))

    return '\n\n'.join(rhyme)