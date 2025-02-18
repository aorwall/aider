def recite(start_verse, end_verse):
    verses = {
        1: "this is the house that Jack built.",
        2: "this is the malt that lay in the house that Jack built.",
        3: "this is the rat that ate the malt that lay in the house that Jack built.",
        4: "this is the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        5: "this is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        6: "this is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        7: "this is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        8: "this is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        9: "this is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        10: "this is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        11: "this is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        12: "this is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        # Additional verses can be added as needed
    }

    rhyme = []
    for i in range(start_verse, end_verse + 1):
        if i in verses:
            rhyme.append(" ".join(word.capitalize() for word in verses[i].split(' ')))

    return '\n'.join(rhyme)
