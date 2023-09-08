import re
from collections import Counter

def count_words(sentence):
    # Remove punctuation and convert to lowercase
    sentence = re.sub(r'[^\w\s]', '', sentence).lower()
    
    # Split the sentence into words
    words = re.findall(r'\b\w+\b', sentence)
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    return dict(word_counts)

# Example usage
sentence = "That's the password: 'PASSWORD 123'!\nSo I fled."
print(count_words(sentence))
