# 36. Write a Python function to calculate the sum of a list of numbers.

def sum_list(a):
    s = sum(a)
    return s

lista = [1,2,3,4,5,6,7,8,9,10]
print(f"The sum is: {sum_list(lista)}")