import re

def count_words(sentence):
    words = re.split(r"\W+", sentence.lower())
    word_counts = {}
    
    for word in words:
        word = word.strip(".:;?!-")
        if word:
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1
        
    return word_counts
