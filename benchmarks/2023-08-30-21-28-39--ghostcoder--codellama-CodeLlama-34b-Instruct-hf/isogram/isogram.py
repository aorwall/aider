def is_isogram(string):
    # Check if the string contains any duplicate characters
    for char in string:
        if string.count(char) > 1:
            return False
    return True
