import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / denominator, (self.imaginary * other.real - self.real * other.imaginary) / denominator)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        abs_value = self.__abs__()
        cos_value = math.cos(self.imaginary)
        sin_value = math.sin(self.imaginary)
        return ComplexNumber(cos_value, sin_value) * (math.e ** self.real)

# Test cases
c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)

assert c1 + c2 == ComplexNumber(4, 6)
assert c1 - c2 == ComplexNumber(-2, -2)
assert c1 * c2 == ComplexNumber(-5, 10)
assert c1 / c2 == ComplexNumber(13/25, 2/25)
assert abs(c1) == 2.23606797749979
assert c1.conjugate() == ComplexNumber(1, -2)
assert c1.exp() == ComplexNumber(-1.46927988357548, 2.422079264594009)
