# 29. Write a Python class to represent a complex number, including 
# methods for addition and subtraction of complex numbers.

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    

num1 = ComplexNumber(2, 7)
num2 = ComplexNumber(1, 4)

print(f"First complex number: {num1}")
print(f"Second complex number: {num2}")

addition_result = num1 + num2

print(f"Addition: {addition_result}")

subtraction_result = num1 - num2

print(f"Subtraction: {subtraction_result}")
