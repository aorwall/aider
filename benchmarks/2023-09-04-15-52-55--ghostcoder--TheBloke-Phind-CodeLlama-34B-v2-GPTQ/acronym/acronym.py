import re

def abbreviate(words):
    words = re.sub('[^A-Za-z0-9 ]+', '', words) # Remove punctuation except space
    words = words.split() # Split into separate words
    acronym = ''.join([word[0].upper() for word in words]) # Take first letter of each word
    return acronym
