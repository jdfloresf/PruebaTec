"""
7. Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números 
de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def sum(arr) -> int:
    result = 0
    for i in arr:
        result += i
    print(f"La suma es: {result}")

def multiplicacion(arr) -> int:
    result = arr[0]
    for i in arr:
        result *= i
    print(f"La multiplicacion es: {result}")

lista = [1, 2 ,3 ,4]
sum(lista)
multiplicacion(lista)