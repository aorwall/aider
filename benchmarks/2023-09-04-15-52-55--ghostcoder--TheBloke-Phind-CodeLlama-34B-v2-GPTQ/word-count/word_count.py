import re
from collections import defaultdict

def count_words(sentence):
    # Use regex to split the sentence into words while preserving the apostrophe in contractions
    words = re.findall(r"\b\w+(?:\'\w+)?\b", sentence)

    # Convert all words to lowercase for case insensitivity
    words = [word.lower() for word in words]

    # Create a dictionary where the keys are words and their values are their occurrence count
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    return dict(word_count)
