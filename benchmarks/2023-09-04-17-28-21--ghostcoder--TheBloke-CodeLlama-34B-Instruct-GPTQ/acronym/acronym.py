import re

def abbreviate(phrase):
    # Remove any non-word characters
    phrase = re.sub(r'\W', '', phrase)

    # Split the phrase into individual words
    words = phrase.split()

    # Create an empty string to store the acronym
    acronym = ""

    # Iterate over each word in the phrase
    for word in words:
        # Add the first letter of each word to the acronym
        acronym += word[0].upper()

    # Return the computed acronym
    return acronym