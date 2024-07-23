# 48. Write a Python program to remove the ith element from a list.

lista = [10, 20, 30, 40, 50]
print(f"Original list: {lista}")
index = 2

if index < 0 or index >= len(lista):
    raise IndexError("Index out of range.")
del lista[index]

updated_list = lista
print(f"Updated list after removing element at index {index}: {updated_list}")
