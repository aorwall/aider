def is_isogram(string):
    # Convert the string to lowercase
    string = string.lower()

    # Create a set to store the unique characters
    unique_chars = set()

    # Iterate through each character in the string
    for char in string:
        # Check if the character is a letter
        if char.isalpha():
            # Check if the character is already in the set
            if char in unique_chars:
                return False
            else:
                unique_chars.add(char)

    return True