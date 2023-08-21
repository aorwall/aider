def recite(start_verse, end_verse):
    # List of animals in the song
    animals = [
        "fly",
        "spider",
        "bird",
        "cat",
        "dog",
        "goat",
        "cow",
        "horse"
    ]

    # List of phrases for each animal
    phrases = [
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "It wriggled and jiggled and tickled inside her.",
        "How absurd to swallow a bird!",
        "Imagine that, to swallow a cat!",
        "What a hog, to swallow a dog!",
        "Just opened her throat and swallowed a goat!",
        "I don't know how she swallowed a cow!",
        "She's dead, of course!"
    ]

    # Initialize the song lyrics
    song = []

    # Iterate over the verses
    for verse in range(start_verse, end_verse + 1):
        # Get the current animal and phrase
        animal = animals[verse - 1]
        phrase = phrases[verse - 1]

        # Add the first line of the verse
        song.append(f"I know an old lady who swallowed a {animal}.")

        # Check if it's not the last verse
        if verse != end_verse:
            # Iterate over the previous animals in reverse order
            for i in range(verse - 1, 0, -1):
                # Get the previous animal
                prev_animal = animals[i - 1]

                # Add the line for swallowing the previous animal
                song.append(f"She swallowed the {animal} to catch the {prev_animal}{phrases[i]}")

        # Add the last line of the verse
        if verse != 1:
            song.append(phrases[0])

        # Add an empty line between verses
        song.append("")

    # Remove the last empty line
    song.pop()

    # Return the song lyrics as a string
    return "\n".join(song)