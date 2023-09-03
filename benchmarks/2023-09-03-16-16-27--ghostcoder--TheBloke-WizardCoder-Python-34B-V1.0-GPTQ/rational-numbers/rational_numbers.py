from math import gcd

def lcm(x, y):
    """Return least common multiple."""
    return x * y // gcd(x, y)


class Rational:
    ...

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)
