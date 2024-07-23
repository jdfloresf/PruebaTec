# Write a Python program to unpack a tuple into several variables.

tupla = (1, 31.31, "hola", [1,2,3,4], (3,4,5), {1:"one", 2:"two", 3:"three"}, True)

integer = tupla[0]
float_n = tupla[1]
string = tupla[2]
lista = tupla[3]
tupla_unpack = tupla[4]
dictionary = tupla[5]
boolean = tupla[6]


print(f"Integer: {integer}")
print(f"Float: {float_n}")
print(f"String: {string}")
print(f"List: {lista}")
print(f"Nested Tuple: {tupla_unpack}")
print(f"Dictionary: {dictionary}")
print(f"Boolean: {boolean}")
