from math import gcd

def reduce_rational(numer, denom):
    if denom < 0:
        numer, denom = -numer, -denom
    gcd_value = gcd(abs(numer), denom)
    return numer // gcd_value, denom // gcd_value

class Rational:
    def __init__(self, numer, denom):
        self.numer, self.denom = reduce_rational(numer, denom)

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numer == other.numer and self.denom == other.denom
        elif isinstance(other, int):
            return self.numer == other and self.denom == 1
        else:
            return False

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.denom + self.denom * other.numer
            denom = self.denom * other.denom
        elif isinstance(other, int):
            numer = self.numer + self.denom * other
            denom = self.denom
        else:
            return NotImplemented
        return Rational(numer, denom)

    def __sub__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.denom - self.denom * other.numer
            denom = self.denom * other.denom
        elif isinstance(other, int):
            numer = self.numer - self.denom * other
            denom = self.denom
        else:
            return NotImplemented
        return Rational(numer, denom)

    def __mul__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.numer
            denom = self.denom * other.denom
        elif isinstance(other, int):
            numer = self.numer * other
            denom = self.denom
        else:
            return NotImplemented
        return Rational(numer, denom)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numer == 0:
                raise ZeroDivisionError("division by zero")
            numer = self.numer * other.denom
            denom = self.denom * other.numer
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            numer = self.numer
            denom = self.denom * other
        else:
            return NotImplemented
        return Rational(numer, denom)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
        if isinstance(power, int):
            if power > 0:
                numer = self.numer ** power
                denom = self.denom ** power
            elif power < 0:
                numer = self.denom ** abs(power)
                denom = self.numer ** abs(power)
            else:
                return Rational(1, 1)
        elif isinstance(power, float):
            return (self.numer ** power) / (self.denom ** power)
        else:
            raise TypeError("power must be an integer or a float")
        return Rational(numer, denom)

    def __rpow__(self, base):
        if isinstance(base, int):
            numer = base ** self.numer
            denom = base ** self.denom
        else:
            raise TypeError("base must be an integer")
        return Rational(numer, denom)
