# 90. Write a Python program to find the intersection of two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

# Find the intersection of the two sets
intersection_set = set1.intersection(set2)

common_elements = list(intersection_set)

print(f"Intersection of the two lists: {common_elements}")