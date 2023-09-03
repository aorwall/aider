class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass


def test_rational_numbers():
    r1 = Rational(1, 2)
    r2 = Rational(2, 3)
    assert r1 + r2 == Rational(5, 6)
    assert r1 - r2 == Rational(-1, 6)
    assert r1 * r2 == Rational(1, 3)
    assert r1 / r2 == Rational(3, 4)
    assert abs(r1) == Rational(1, 2)
    assert r1 ** 2 == Rational(1, 4)
    assert 2 ** r1 == Rational(2, 1)


if __name__ == "__main__":
    test_rational_numbers()
