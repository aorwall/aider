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
        if other.real == 0 and other.imaginary == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2), (self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2))

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(math.exp(self.real) * math.cos(self.imaginary), math.exp(self.real) * math.sin(self.imaginary))
