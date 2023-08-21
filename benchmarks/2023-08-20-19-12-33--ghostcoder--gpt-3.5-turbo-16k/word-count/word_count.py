import re

def count_words(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Replace all punctuation marks with whitespace
    sentence = re.sub(r"[^\w\s']", " ", sentence)

    # Split the sentence into words
    words = sentence.split()

    # Count the occurrences of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count