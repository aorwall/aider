def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("Number out of range")
        
    if number < 100:
        # handle 0-99
        pass
        
    return ""
