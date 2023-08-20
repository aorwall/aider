def abbreviate(words):
    # Remove all punctuation except hyphens
    words = ''.join(c for c in words if c.isalnum() or c == '-')

    # Split the words by whitespace or hyphens
    words = words.split()

    # Get the first letter of each word and convert to uppercase
    acronym = ''.join(word[0].upper() for word in words)

    return acronym
