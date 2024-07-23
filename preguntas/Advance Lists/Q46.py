# 46. Write a Python program to find all possible subsets of a list.

import itertools

lista = [1, 2, 3]

subsets = []
for i in range(len(lista) + 1):
    for subset in itertools.combinations(lista, i):
        subsets.append(list(subset))

print("Original list:", lista)
print("All possible subsets:")
for subset in subsets:
    print(subset)
