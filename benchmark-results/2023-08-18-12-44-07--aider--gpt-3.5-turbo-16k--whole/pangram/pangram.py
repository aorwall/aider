def is_pangram(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Create a set to store the unique letters in the sentence
    letters = set()

    # Iterate over each character in the sentence
    for char in sentence:
        # Check if the character is a letter
        if char.isalpha():
            # Add the letter to the set
            letters.add(char)

    # Check if all 26 letters are present in the set
    return len(letters) == 26
