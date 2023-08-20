def is_isogram(string):
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()

    # Create a set to store the unique letters in the string
    letters = set()

    # Iterate through each character in the string
    for char in string:
        # Ignore spaces and hyphens
        if char != ' ' and char != '-':
            # If the character is already in the set, it is a repeated letter
            if char in letters:
                return False
            # Add the character to the set
            letters.add(char)

    # If no repeated letters are found, it is an isogram
    return True
