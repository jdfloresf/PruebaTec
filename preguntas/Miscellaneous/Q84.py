# 84. Write a Python program to remove the kth element from a list.

lst = [10, 20, 30, 40, 50]
k = 2  # Index of the element to remove (0-based index)

if k < 0 or k >= len(lst):
    raise IndexError("Index out of range")

# Remove the k-th element and return the modified list

try:
    print(f"Original list: {lst}")
    lst.pop(k)  
    print(f"List after removing the {k} element: {lst}")
except IndexError as e:
    print(e)