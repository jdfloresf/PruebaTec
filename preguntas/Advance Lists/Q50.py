# 50. Write a Python program to sort a list of tuples 
# based on the second element.

tuples_list = [(1, 3), (2, 1), (3, 2), (4, 4), (12,9), (1, 1)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])


print("Original list of tuples:", tuples_list)
print("Sorted list of tuples:", sorted_list)
