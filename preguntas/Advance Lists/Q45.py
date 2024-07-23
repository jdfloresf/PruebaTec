# 45. Write a Python program to generate all permutations of a list.

import itertools

lista = [1, 2, 3]

permutations = list(itertools.permutations(lista))
print("Original list:", lista)

print("Permutations:")
for perm in permutations:
    print(perm)
