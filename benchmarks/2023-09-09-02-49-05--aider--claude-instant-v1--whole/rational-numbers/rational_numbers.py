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

    def reduce(self):
        gcd = math.gcd(int(self.numer), int(self.denom)) 
        self.numer //= gcd
        self.denom //= gcd
        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1

    def __add__(self, other):
        n = self.numer*other.denom + other.numer*self.denom
        d = self.denom*other.denom
        return Rational(n, d)

    def __sub__(self, other):
        n = self.numer*other.denom - other.numer*self.denom
        d = self.denom*other.denom
        return Rational(n, d)

    def __mul__(self, other):
        n = self.numer*other.numer
        d = self.denom*other.denom
        return Rational(n, d)

    def __truediv__(self, other):
        n = self.numer*other.denom
        d = self.denom*other.numer
        return Rational(n, d)

    def __abs__(self):
        n = abs(self.numer)
        d = self.denom
        return Rational(n, d)

    def __pow__(self, power):
        n = int(self.numer)**power 
        d = int(self.denom)**power
        return Rational(n, d)

    def __rpow__(self, base):
        return base**(self.numer/self.denom)
