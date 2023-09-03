def response(hey_bob):
    # Checking for question
    if hey_bob.endswith('?'):
        return "Sure."

    # Checking for yell
    elif hey_bob == hey_bob.upper():
        return "Whoa, chill out!"

    # Checking for yelled question
    elif hey_bob.endswith('?') and hey_bob != hey_bob.lower():
        return "Calm down, I know what I'm doing!"

    # Checking for silence
    elif hey_bob.strip() == '':
        return "Fine. Be that way!"

    # Default case
    else:
        return "Whatever."
