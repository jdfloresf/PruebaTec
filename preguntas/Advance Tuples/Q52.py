# 52. Write a Python program to convert a tuple of tuples to a dictionary.


tuple_of_tuples = (('a', 1), ('b', 2), ('c', 3))
dictionary = {key: value for key, value in tuple_of_tuples}

print(f"Tuple of tuples: {tuple_of_tuples}")
print(f"Dictionary: {dictionary}")
