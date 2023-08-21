import string

def count_words(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Replace all punctuation except apostrophes with whitespace
    translator = str.maketrans(string.punctuation.replace("'", ""), ' '*len(string.punctuation.replace("'", "")))
    sentence = sentence.translate(translator)

    # Split the sentence into words
    words = sentence.split()

    # Count the frequency of each word
    word_count = {}
    for word in words:
        # Remove leading and trailing apostrophes from each word
        word = word.strip("'")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
