def is_isogram(string):
    string = string.replace(' ', '').replace('-', '')
    return len(string) == len(set(string))
