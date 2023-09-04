def response(hey_bob):
    if hey_bob.endswith('?'):
        return 'Sure.'
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    elif hey_bob.startswith('WHAT'):
        return 'Calm down, I know what I\'m doing!'
    elif len(hey_bob) <= 0:
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
