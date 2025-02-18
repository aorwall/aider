import re
from collections import defaultdict
def count_words(sentence):
    # Use a regular expression to split the sentence into words.
    # \b is a zero-width assertion that matches a word boundary.
    # This ensures that contractions like "it's" are considered one word.
    words = re.findall(r'\b\w+\b', sentence)

    # Create a dictionary where the keys are words and the values are their counts.
    word_counts = defaultdict(int)

    # Iterate over each word in the list of words.
    for word in words:
        # Convert the word to lowercase to ensure case insensitivity.
        word = word.lower()

        # Increment the count of the current word in the dictionary.
        word_counts[word] += 1

    return dict(word_counts)
