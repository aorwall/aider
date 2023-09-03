import random

def private_key(p):
    """Return a randomly chosen integer between 2 and p - 1"""
    return random.randint(2, p - 1)


def public_key(p, g, private):
    """Calculate the public key given a private key and base g"""
    return pow(g, private, p)


def secret(p, public, private):
    """Calculate the shared secret key given both parties' private keys"""
    return pow(public, private, p)
