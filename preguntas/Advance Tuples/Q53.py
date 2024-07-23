# 53. Write a Python program to sort a tuple by its float element.


tuples_list = [(1, 3.5), (2, 1.1), (3, 2.8), (4, 4.2)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])

print("Original list of tuples:", tuples_list)
print("Sorted list of tuples:", sorted_list)
