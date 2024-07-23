# 89. Write a Python program to find the product of all elements in a list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prod = lst[0]
for n in lst:
    prod *= n

print(f"List: {lst}")
print(f"Product: {prod}")