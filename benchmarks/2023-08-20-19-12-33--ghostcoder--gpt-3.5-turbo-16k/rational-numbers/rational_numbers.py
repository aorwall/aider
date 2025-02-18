class Rational:
    def __init__(self, numer, denom):
        gcd = self._gcd(numer, denom)
        self.numer = numer // gcd
        self.denom = denom // gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __sub__(self, other):
        new_numer = self.numer * other.denom - other.numer * self.denom
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
        new_numer = abs(self.numer)
        new_denom = abs(self.denom)
        return Rational(new_numer, new_denom)

    def __pow__(self, power):
        if power >= 0:
            new_numer = self.numer ** power
            new_denom = self.denom ** power
        else:
            new_numer = self.denom ** abs(power)
            new_denom = self.numer ** abs(power)
        return Rational(new_numer, new_denom)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a