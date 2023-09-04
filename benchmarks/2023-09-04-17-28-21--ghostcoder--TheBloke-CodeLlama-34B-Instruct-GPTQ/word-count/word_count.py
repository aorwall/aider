import re

def count_words(sentence):
    # Remove punctuations and convert to lowercase
    sentence = re.sub('[^a-zA-Z\d]+', '', sentence).lower()

    # Split the sentence into individual words
    words = sentence.split()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Iterate over the words and increment the count for each one
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    return word_counts
