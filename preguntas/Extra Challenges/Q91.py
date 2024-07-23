# 91. Write a Python program to find the maximum product of two integers
#  in a list.

lst = [1, -10, -5, 2, 3, 4]

if len(lst) < 2:
    raise ValueError("List must contain at least two integers.")

# Sort the list
lst_sorted = sorted(lst)

# Compute the maximum product
product1 = lst_sorted[-1] * lst_sorted[-2]  # Product of the two largest numbers
product2 = lst_sorted[0] * lst_sorted[1]    # Product of the two smallest numbers

max_product = max(product1, product2)

print(f"Maximum product of two integers in the list: {max_product}")