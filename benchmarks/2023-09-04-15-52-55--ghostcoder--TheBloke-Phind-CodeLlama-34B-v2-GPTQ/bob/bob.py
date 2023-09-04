import re

def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"
    elif re.match('^[^?]*\?$', hey_bob) is not None:
        return "Sure."
    elif re.search('[A-Z]+', hey_bob) is not None and hey_bob == hey_bob.upper():
        return "Whoa, chill out!"
    elif re.search('[A-Z]+', hey_bob) is not None:
        return "Calm down, I know what I'm doing!"
    else:
        return "Whatever."
