def is_isogram(string):
    string = string.replace(" ", "").replace("-", "").lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True
