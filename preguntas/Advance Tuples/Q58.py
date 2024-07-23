# 58. Write a Python program to create a dictionary from a tuple

tuple_of_pairs = (('name', 'Alice'), ('age', 30), ('city', 'New York'))

if all(isinstance(i, tuple) and len(i) == 2 for i in tuple_of_pairs):
    dictionary = dict(tuple_of_pairs)
else:
    raise ValueError("The tuple must contain 2-element tuples.")

print("Dictionary:", dictionary)
