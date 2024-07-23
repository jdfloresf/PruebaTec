# 65. Write a Python class to represent a polynomial and implement methods 
# for polynomial addition and multiplication.

class Polynomial:
    def __init__(self, coefficients):
        """Initialize the polynomial with a list of coefficients.
           coefficients[i] represents the coefficient for the x^i term.
        """
        self.coefficients = coefficients

    def __add__(self, other):
        """Add two polynomials and return a new polynomial."""
        max_len = max(len(self.coefficients), len(other.coefficients))
        result_coefficients = [0] * max_len

        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            result_coefficients[i] = coeff1 + coeff2

        return Polynomial(result_coefficients)

    def __mul__(self, other):
        """Multiply two polynomials and return a new polynomial."""
        result_len = len(self.coefficients) + len(other.coefficients) - 1
        result_coefficients = [0] * result_len

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(result_coefficients)

    def __str__(self):
        """Return a string representation of the polynomial."""
        terms = []
        for power, coeff in enumerate(self.coefficients):
            if coeff == 0:
                continue
            if power == 0:
                terms.append(str(coeff))
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{power}")
        return " + ".join(terms) if terms else "0"


p1 = Polynomial([1, 2, 3])  # Represents 1 + 2x + 3x^2
p2 = Polynomial([3, 4, 5])  # Represents 3 + 4x + 5x^2
print("P1:", p1)
print("P2:", p2)
p3 = p1 + p2
print("P1 + P2:", p3)
p4 = p1 * p2
print("P1 * P2:", p4)
