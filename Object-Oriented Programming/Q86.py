class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = self.real + other.real
            imaginary_part = self.imaginary + other.imaginary
            return ComplexNumber(real_part, imaginary_part)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = self.real - other.real
            imaginary_part = self.imaginary - other.imaginary
            return ComplexNumber(real_part, imaginary_part)
        return NotImplemented
real1 = float(input("Enter the real part of the first complex number: "))
imaginary1 = float(input("Enter the imaginary part of the first complex number: "))
real2 = float(input("Enter the real part of the second complex number: "))
imaginary2 = float(input("Enter the imaginary part of the second complex number: "))
complex1 = ComplexNumber(real1, imaginary1)
complex2 = ComplexNumber(real2, imaginary2)
sum_result = complex1 + complex2
difference_result = complex1 - complex2
print(f"Complex 1: {complex1}")
print(f"Complex 2: {complex2}")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")