def recite(start_verse, end_verse):
    # Define the phrases for each verse
    phrases = [
        "the house that Jack built.",
        "the malt\nthat lay in " + phrases[0],
        "the rat\nthat ate " + phrases[1],
        "the cat\nthat killed " + phrases[2],
        "the dog\nthat worried " + phrases[3],
        "the cow with the crumpled horn\nthat tossed " + phrases[4],
        "the maiden all forlorn\nthat milked " + phrases[5],
        "the man all tattered and torn\nthat kissed " + phrases[6],
        "the priest all shaven and shorn\nthat married " + phrases[7],
        "the rooster that crowed in the morn\nthat woke " + phrases[8],
        "the farmer sowing his corn\nthat kept " + phrases[9],
        "the horse and the hound and the horn\nthat belonged to " + phrases[10]
    ]

    # Get the selected verses
    selected_phrases = phrases[start_verse - 1:end_verse]

    # Build the final rhyme by joining the selected phrases
    rhyme = "This is " + selected_phrases[0]
    for i in range(1, len(selected_phrases)):
        rhyme += "\n\n" + "This is " + selected_phrases[i]

    return rhyme
