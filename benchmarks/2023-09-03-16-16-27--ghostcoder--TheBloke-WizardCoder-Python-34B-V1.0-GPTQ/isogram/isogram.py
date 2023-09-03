import re

def is_isogram(string):
    # Convert string to lower case and remove non-alphabetical characters
    string = re.sub('[^a-zA-Z]', '', string).lower()

    # Create a set of unique letters in the string
    unique_letters = set(string)

    # Check if length of set is same as length of string
    return len(unique_letters) == len(string)
