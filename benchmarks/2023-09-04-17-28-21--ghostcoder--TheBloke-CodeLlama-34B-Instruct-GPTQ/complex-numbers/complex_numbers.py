import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __repr__(self):
        if self.imaginary < 0:
            return f"{self.real} - {abs(self.imaginary)}i"
        else:
            return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        real = math.exp(self.real) * math.cos(self.imaginary)
        imaginary = math.exp(self.real) * math.sin(self.imaginary)
        return ComplexNumber(real, imaginary)

if __name__ == "__main__":
    z1 = ComplexNumber(3, 4)
    print(f"z1 = {z1}")
    z2 = ComplexNumber(-1, 5)
    print(f"z2 = {z2}")
    print(f"z1 + z2 = {z1 + z2}")
    print(f"z1 - z2 = {z1 - z2}")
    print(f"z1 * z2 = {z1 * z2}")
    print(f"z1 / z2 = {z1 / z2}")
    print(f"Absolute value of z1 is {abs(z1)}")
    print(f"Conjugate of z1 is {z1.conjugate()}")
    print(f"Exponential of z1 is {z1.exp()}")
