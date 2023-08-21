import re

def abbreviate(words):
    # Remove all punctuation except hyphens and underscores
    words = re.sub(r'[^\w\s-]', '', words)
    
    # Split the words by whitespace and hyphens
    words = re.split(r'[\s-]+', words)
    
    # Get the first letter of each word and convert to uppercase
    acronym = [word[0].upper() for word in words]
    
    # Join the letters to form the acronym
    acronym = ''.join(acronym)
    
    return acronym