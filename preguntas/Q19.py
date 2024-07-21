# Write a Python program to remove an item from a tuple.

tupla = (31.31, "hola", [1,2,3,4], 123, 
         {1:"one", 2:"two", 3:"three"}, True)

item_remove = 123

new_tuple = tuple(x for x in tupla if x != item_remove)

print(new_tuple)

