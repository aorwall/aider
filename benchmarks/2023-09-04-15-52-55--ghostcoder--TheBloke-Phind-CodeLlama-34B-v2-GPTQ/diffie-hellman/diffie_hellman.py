import math
from Crypto import Random

def private_key(p):
    """Generate a private key"""
    while True:
        private = Random.get_random_bytes(5)
        private = int.from_bytes(private, 'big') % (p - 1) + 1

        if math.gcd(private, p - 1) == 1:
            break

    return private


def public_key(p, g, private):
    """Calculate the public key based on private key"""
    return pow(g, private, p)


def secret(p, public, private):
    """Calculate the shared secret between Alice and Bob"""
    return pow(public, private, p)
