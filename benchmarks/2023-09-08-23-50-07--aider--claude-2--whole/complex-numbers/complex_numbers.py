import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        elif isinstance(other, (int, float)):
            return self.real == other and self.imaginary == 0

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imaginary)

    def __radd__(self, other):
        return self.__add__(other)
            
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                                 self.imaginary * other.real + self.real * other.imaginary)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imaginary * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imaginary)
            
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(other - self.real, -self.imaginary)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denom = other.real**2 + other.imaginary**2
            return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / denom,
                                 (self.imaginary * other.real - self.real * other.imaginary) / denom)
        elif isinstance(other, (int, float)):
            denom =