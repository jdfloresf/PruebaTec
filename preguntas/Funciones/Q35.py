# 35. Write a Python function to implement the Fibonacci 
# sequence using recursion.

def fibonacci(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
num = 6
print(f"The {num} Fibonacci number is {fibonacci(num)}")
