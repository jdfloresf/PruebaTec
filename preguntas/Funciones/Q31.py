# 31. Write a Python function to find the greatest 
# common divisor (GCD) of two numbers.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n1 = 72
n2 = 27

print(f"The GCD of {n1} and {n2} is {gcd(n1, n2)}")
