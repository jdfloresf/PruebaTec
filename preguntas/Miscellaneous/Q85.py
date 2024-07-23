# 85. Write a Python program to find the cumulative product of a list.

lst = [1, 2, 3, 4]

if not lst:
    raise  "List is empty"

cum_prod = []
product = 1
for num in lst:
    product *= num
    cum_prod.append(product)

print(f"List: {lst}")
print(f"Cumulative product of the list: {cum_prod}")
