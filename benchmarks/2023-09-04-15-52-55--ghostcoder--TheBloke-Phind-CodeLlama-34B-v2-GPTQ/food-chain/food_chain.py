def recite(start_verse, end_verse):
    verses = {
        0: "I know an old lady who swallowed a fly.",
        1: "I don't know why she swallowed the fly. Perhaps she'll die.",
        2: "I know an old lady who swallowed a spider.\n" + 
           "It wriggled and jiggled and tickled inside her.",
        3: "She swallowed the spider to catch the fly.",
        4: "I know an old lady who swallowed a bird.\n" + 
           "How absurd to swallow a bird!",
        5: "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        6: "She swallowed the spider to catch the fly.",
        7: "I know an old lady who swallowed a cat.\n" + 
           "Imagine that, to swallow a cat!",
        8: "She swallowed the cat to catch the bird.",
        9: "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        10: "She swallowed the spider to catch the fly.",
        11: "I know an old lady who swallowed a dog!\n" + 
            "What a hog, to swallow a dog!",
        12: "She swallowed the dog to catch the cat.",
        13: "She swallowed the cat to catch the bird.",
        14: "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        15: "She swallowed the spider to catch the fly.",
        16: "I know an old lady who swallowed a goat!\n" + 
             "Just opened her throat and swallowed a goat!",
        17: "She swallowed the goat to catch the dog.",
        18: "She swallowed the dog to catch the cat.",
        19: "She swallowed the cat to catch the bird.",
        20: "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        21: "She swallowed the spider to catch the fly.",
        22: "I know an old lady who swallowed a cow.\n" + 
             "I don't know how she swallowed a cow!",
        23: "She's dead, of course!"
    }

    result = []
    for i in range(start_verse - 1, end_verse):
        result.append(verses[i % 24]) # Verses are numbered from 1 to 24, so we need to modulo by 24
    return "\n\n".join(result)
