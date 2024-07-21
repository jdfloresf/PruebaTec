# Write a Python program to find the common elements in two lists.

lista1 = [1,2,3,4,5]
lista2 = [4,87,3,10,9]

common = [n for n in lista1 if n in lista2]

print(f"Common: {common}")