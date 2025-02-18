import math
class Rational:
    def __init__(self, numer, denom=1):
        if denom == 0:
            raise ZeroDivisionError('division by zero')
        elif denom < 0:
            numer, denom = -numer, abs(denom)
        gcd = math.gcd(abs(numer), abs(denom))
        self.numer = numer // gcd
        self.denom = denom // gcd
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        self.numer = numer // gcd
        self.denom = denom // gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        if self.denom == 1:
            return str(self.numer)
        else:
            return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ZeroDivisionError('division by zero')
        elif other.numer < 0:
            return -(-self / (-other))
        else:
            return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int):
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational((self.numer ** abs(power)) * (abs(self.denom) ** power), (self.denom ** abs(power)) * (abs(self.numer) ** power))

    def __rpow__(self, base):
        if base < 0 and not math.isclose(math.log(base).imag % 1, 0.5):
            return complex(self.__pow__(complex(base)))
        else:
            return Rational((base ** self.numer) // (base ** self.denom), 1)
