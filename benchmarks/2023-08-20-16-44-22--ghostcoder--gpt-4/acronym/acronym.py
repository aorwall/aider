import string

def abbreviate(words):
    # Replace hyphens with spaces and remove all other punctuation
    words = words.replace('-', ' ').translate(str.maketrans('', '', string.punctuation))
    # Split the string into words, take the first character of each word, convert it to uppercase, and join them together
    return ''.join(word[0].upper() for word in words.split())