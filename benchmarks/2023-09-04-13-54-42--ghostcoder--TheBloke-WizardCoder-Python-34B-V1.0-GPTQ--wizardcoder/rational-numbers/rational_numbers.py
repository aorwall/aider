def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class Rational:
    def __init__(self, numer, denom):
        common = gcd(numer, denom)
        self.numer = numer // common
        self.denom = denom // common

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        new_numer = self.numer * other.denom + self.denom * other.numer
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __sub__(self, other):
        new_numer = self.numer * other.denom - self.denom * other.numer
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __mul__(self, other):
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __truediv__(self, other):
        new_numer = self.numer * other.denom
        new_denom = self.denom * other.numer
        return Rational(new_numer, new_denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int):
            result = Rational(1, 1)
            for i in range(abs(power)):
                result *= self
            if power < 0:
                result = 1 / result
            return result
        else:
            raise TypeError("Only integers supported as exponents")

    def __rpow__(self, base):
        if self.denom == 1 and base > 0:
            return base ** self.numer
        elif self.denom == 1 and base < 0:
            return (-base) ** self.numer
        else:
            raise ValueError("Base must be positive or negative with an integer denominator.")
