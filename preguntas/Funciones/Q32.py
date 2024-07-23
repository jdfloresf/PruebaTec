# 32. Write a Python function to find the least common 
# multiple (LCM) of two numbers.

from Q31 import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)


n1 = 48
n2 = 18

print(f"The LCM of {n1} and {n2} is {lcm(n1, n2)}")
