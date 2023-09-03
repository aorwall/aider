def abbreviate(words):
    """
    Convert a phrase to its acronym.

    Args:
        words (str): The phrase to convert.

    Returns:
        str: The acronym of the phrase.
    """
    # Remove punctuation
    words = words.replace("-", " ").strip()

    # Extract the first letter of each word
    acronym = ""
    for word in words.split():
        acronym += word[0]

    return acronym.upper()