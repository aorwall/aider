import re
from collections import Counter

def count_words(sentence):
    # Remove all non-alphanumeric characters except apostrophes
    cleaned_sentence = re.sub(r"[^a-zA-Z0-9\s']", "", sentence)

    # Split into individual words
    words = re.findall(r"\b\w+\b|\d+", cleaned_sentence)

    # Count occurrences of each word
    word_counter = Counter(words)

    return dict(word_counter)

# Test cases
assert count_words("That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I flew.") == {
    "'": 1,
    "Agent": 1,
    "I": 1,
    "Special": 1,
    "So": 1,
    "flew": 1,
    "password": 2,
    "the": 2,
    "thats": 1,
    "123": 1,
}
print(count_words("That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I flew."))
# Output should be {'123': 1, 'agent': 1, 'cried': 1, 'flew': 1, 'i': 1, 'password': 2, 'so': 1, 'special': 1, 'that\'s': 1, 'the': 2}
