# 34. Write a Python function to find the factorial of a 
# number using recursion.

def factorial(a):
    if a == 0 or a == 1:
        return 1

    return a * factorial(a - 1)


num = 5
print(f"The factorial of {num} is {factorial(num)}")