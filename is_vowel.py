"""
6 Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def is_vocal(caracter: str) -> str:
    vocales = ['a', 'e', 'i', 'o', 'u']
    return True if caracter in vocales else False

print(f"Es vocal: {is_vocal('a')}")
print(f"Es vocal: {is_vocal('p')}")