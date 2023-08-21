verses = [
    ("fly", "", "I don't know why she swallowed the fly. Perhaps she'll die."),
    ("spider", "It wriggled and jiggled and tickled inside her.", "She swallowed the spider to catch the fly."),
    ("bird", "How absurd to swallow a bird!", "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."),
    ("cat", "Imagine that, to swallow a cat!", "She swallowed the cat to catch the bird."),
    ("dog", "What a hog, to swallow a dog!", "She swallowed the dog to catch the cat."),
    ("goat", "Just opened her throat and swallowed a goat!", "She swallowed the goat to catch the dog."),
    ("cow", "I don't know how she swallowed a cow!", "She swallowed the cow to catch the goat."),
    ("horse", "She's dead, of course!", "")
]

def recite(start_verse, end_verse):
    # Generate the lyrics of the song from start_verse to end_verse
    lyrics = []
    for i in range(start_verse - 1, end_verse):
        animal, comment, action = verses[i]
        verse = f"I know an old lady who swallowed a {animal}."
        if comment:
            verse += f" {comment}"
        if i > 0:
            verse += f" {action}"
        lyrics.append(verse)

    return lyrics
