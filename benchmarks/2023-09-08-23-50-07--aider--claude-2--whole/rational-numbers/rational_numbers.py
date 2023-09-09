import math

class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.reduce()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)

    def __pow__(self, power):
        if isinstance(power, int):
            if power >= 0:
                numer = self.numer ** power 
                denom = self.denom ** power
            else:
                power = -power
                numer = self.denom ** power
                denom = self.numer ** power
        else:
            numer = self.numer ** power
            denom = self.denom ** power
        return Rational(numer, denom)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)

    def reduce(self):
        gcd = math.gcd(self.numer, self.denom)
        self.numer //= gcd
        self.denom //= gcd
        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1
