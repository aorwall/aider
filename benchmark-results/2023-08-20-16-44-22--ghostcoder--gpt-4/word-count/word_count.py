import re
from collections import Counter

def count_words(sentence):
    words = re.findall(r"[a-z0-9]+'[a-z0-9]+|[a-z0-9]+", sentence.lower())
    return dict(Counter(words))