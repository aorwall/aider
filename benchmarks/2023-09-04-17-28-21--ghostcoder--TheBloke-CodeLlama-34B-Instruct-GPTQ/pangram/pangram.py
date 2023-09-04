import re
from collections import Counter

def is_pangram(sentence):
    """
    Check if a sentence is a pangram.
    
    Args:
        sentence (str): Sentence to check.
        
    Returns:
        bool: True if sentence is a pangram, False otherwise.
    """
    # Convert sentence to lowercase
    sentence = sentence.lower()

    # Remove punctuation and spaces
    sentence = re.sub('[^a-z]', '', sentence)

    # Count number of occurrences of each letter
    letter_counts = Counter(sentence)

    # Check if there are exactly 26 unique letters
    return len(letter_counts) == 26
