import re
def count_words(sentence):
    words = re.split(r'\W+', sentence)
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts
