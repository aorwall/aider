def response(hey_bob):
    if hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif hey_bob.strip() == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
