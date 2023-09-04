import math

class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.real == other.real and self.imaginary == other.imaginary
        else:
            return False

    def __repr__(self):
        return f"{self.real} {self.imaginary}i"

    def __add__(self, other):
        return self.__class__(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return self.__class__(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return self.__class__(real, imaginary)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            denominator = other.real ** 2 + other.imaginary ** 2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
            return self.__class__(real, imaginary)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__class__(self.real / other, self.imaginary / other)
        else:
            raise TypeError("unsupported operand type(s) for /")

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return self.__class__(self.real, -self.imaginary)

    def exp(self):
        r = math.exp(self.real)
        return self.__class__(r*math.cos(self.imaginary), r*math.sin(self.imaginary))
