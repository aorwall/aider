import random

def private_key(p):
    # Return a random key between 1 and p-1
    return random.randint(2, p-1)


def public_key(p, g, private):
    return pow(g, private, p)


def secret(p, public, private):
    return pow(public, private, p)
