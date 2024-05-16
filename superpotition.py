"""
10- Definir una función superposicion() que tome dos listas y devuelva True 
si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado.
"""

def superposicion(arr1: list, arr2: list) -> bool:
    for i in arr1:
        for j in  arr2:
            if i == j:
                return True
    return False

lista1 = [1,2,3,4,5]
lista2 = [4,87,3,10,9]
lista3 = [9,0,43,421,7]

print(f"tienen un elemento en comun: {superposicion(lista1, lista2)}")
print(f"tienen un elemento en comun: {superposicion(lista1, lista3)}")
