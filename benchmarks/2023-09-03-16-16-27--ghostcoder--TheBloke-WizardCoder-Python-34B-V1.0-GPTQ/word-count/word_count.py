import re
from collections import Counter

def count_words(sentence):
    # Remove all non-alphanumeric characters except apostrophes and convert to lowercase
    cleaned = re.sub("[^a-zA-Z0-9'\s]+", '', sentence).replace("'", "").lower()

    # Split the string into words
    words = cleaned.split()

    # Count the frequency of each word
    return dict(Counter(words))
