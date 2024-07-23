# 60. Write a Python program to get the n largest elements from a list of tuples.

import heapq

list_of_tuples = [(1, 'a'), (5, 'b'), (3, 'c'), (8, 'd'), (2, 'e')]
n = 3

"""Get the n largest tuples from a list of tuples based on the first element."""
# Ensure n is not greater than the length of the list
n = min(n, len(list_of_tuples))

# Use heapq.nlargest to get the n largest tuples based on the first element
largest_tuples = heapq.nlargest(n, list_of_tuples, key=lambda x: x[0])

print(f"The {n} largest tuples based on the first element are:", largest_tuples)
