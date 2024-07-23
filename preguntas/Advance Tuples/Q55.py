# 55. Write a Python program to convert a tuple to a dictionary.

tpl = (('a', 1), ('b', 2), ('c', 3))

if all(isinstance(i, tuple) and len(i) == 2 for i in tpl):
    dictionary = dict(tpl)
else:
    raise ValueError("The tuple must contain 2-element tuples.")


print("Dictionary:", dictionary)
