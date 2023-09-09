def trinary(string):
    if not string.isnumeric() or set(string) - set("012"):
        return 0
    
    value = 0
    place = len(string)-1
    for char in string:
        value += int(char) * 3**place
        place -= 1
        
    return value
