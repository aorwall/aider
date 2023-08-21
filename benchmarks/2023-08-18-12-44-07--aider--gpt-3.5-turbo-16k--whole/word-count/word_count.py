def count_words(sentence):
    # Initialize an empty dictionary to store the word counts
    word_counts = {}

    # Split the sentence into words using whitespace and punctuation as separators
    words = sentence.split()

    # Iterate over each word
    for word in words:
        # Remove any leading or trailing punctuation from the word
        word = word.strip(",:!?'\"")

        # Convert the word to lowercase to make it case insensitive
        word = word.lower()

        # If the word is already in the dictionary, increment its count by 1
        if word in word_counts:
            word_counts[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            word_counts[word] = 1

    # Remove any empty strings from the word counts dictionary
    word_counts = {word: count for word, count in word_counts.items() if word}

    # Return the word counts dictionary
    return word_counts
