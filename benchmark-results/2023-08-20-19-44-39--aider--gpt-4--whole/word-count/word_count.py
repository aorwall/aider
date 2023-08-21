import re
from collections import Counter

def count_words(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"(?<!\w)'|'(?!\w)", ' ', sentence)
    sentence = re.sub(r"[^\w\s]", ' ', sentence)
    words = sentence.split()
    return dict(Counter(words))
