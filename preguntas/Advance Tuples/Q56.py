# 56. Write a Python program to check if a specified element is present 
# in a tuple of tuples.

tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
element = 5

for tpl in tuple_of_tuples:
    if element in tpl:
        result = True
result = False


print(f"Is {element} present in the tuple of tuples? {result}")
