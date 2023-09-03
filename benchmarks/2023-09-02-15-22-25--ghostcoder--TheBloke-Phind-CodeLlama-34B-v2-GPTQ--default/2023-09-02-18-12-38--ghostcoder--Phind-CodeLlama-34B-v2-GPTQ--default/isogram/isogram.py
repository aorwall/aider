def is_isogram(string):
    string = string.replace(' ', '')
    string = string.replace('-', '')

    return len(string) == len(set(string))
