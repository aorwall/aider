import math
class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        denominator = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / denominator, (self.imaginary * other.real - self.real * other.imaginary) / denominator)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        abs_value = self.__abs__()
        cos_part = round(math.cos(self.imaginary), 4)
        sin_part = round(math.sin(self.imaginary), 4)
        real_part = round(math.e ** self.real * cos_part, 4)
        imaginary_part = round(math.e ** self.real * sin_part, 4)
        return ComplexNumber(real_part, imaginary_part)
