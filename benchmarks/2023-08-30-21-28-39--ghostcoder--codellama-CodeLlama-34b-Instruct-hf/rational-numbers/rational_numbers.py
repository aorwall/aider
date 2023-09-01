class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ZeroDivisionError('division by zero')
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return Rational(base ** self.numer, base ** self.denom)