def response(hey_bob):
    # Check if input contains uppercase letters (i.e., yelling)
    if hey_bob.strip().isupper():
        if '?' in hey_bob:
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif hey_bob == '' or hey_bob.isspace() or len(hey_bob) == 0:
        return "Fine. Be that way!"
    elif '?' in hey_bob[-1]:
        return "Sure."
    else:
        return "Whatever."
