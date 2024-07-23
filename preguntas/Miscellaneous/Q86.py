# 86. Write a Python program to find all prime numbers in a list.

def prime(a):
    count = 0
    flag = False
    for n in range(1, a+1):
        if a % n == 0:
            count += 1

    if count>2:
        return flag
    else:
        flag = True
        return flag


lst = [1, 2, 3, 4, 5, 10, 13, 17, 18, 20, 21, 25, 30, 43]
print(f"Prime numbers in the list: {lst}")
primes = [num for num in lst if prime(num)]
print(f"Primes: {primes}")
