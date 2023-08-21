import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        else:
            return self.real == other and self.imaginary == 0

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real + other.real
            imaginary = self.imaginary + other.imaginary
        else:
            real = self.real + other
            imaginary = self.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imaginary * other.imaginary
            imaginary = self.imaginary * other.real + self.real * other.imaginary
        else:
            real = self.real * other
            imaginary = self.imaginary * other
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real - other.real
            imaginary = self.imaginary - other.imaginary
        else:
            real = self.real - other
            imaginary = self.imaginary
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denominator = other.real ** 2 + other.imaginary ** 2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        else:
            real = self.real / other
            imaginary = self.imaginary / other
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        real_part = math.exp(self.real) * math.cos(self.imaginary)
        imaginary_part = math.exp(self.real) * math.sin(self.imaginary)
        return ComplexNumber(real_part, imaginary_part)
