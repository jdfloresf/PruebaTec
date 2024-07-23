# 33. Write a Python function to check if a number is prime.

def prime(a):
    count = 0
    flag = False
    for n in range(1, a+1):
        if a % n == 0:
            count += 1

    if count>2:
        print(f"{a} is prime: {flag}")
    else:
        flag = True
        print(f"{a} is prime: {flag}")

n = 11

prime(n)
