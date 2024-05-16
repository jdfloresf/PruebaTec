import time


"""
1 Definir una función max() que tome como argumento dos numeros y
devuelva el mayor de ellos.

"""

def custom_max(n1: int, n2: int) -> int:
    """Retorna el mayor de dos numeros

    Args:
        n1 (int): numero 1 a evaluar
        n2 (int): numero 2 a evaluar

    Returns:
        int: mayor de ambos
    """
    if n1 == n2:
        raise Exception("Los numeros no pueden ser iguales")
    return n1 if n1 > n2 else n2

# print("Mayor de dos numeros")
# print(custom_max(5,9), '\n')

"""
2 Definir una función max_de_tres() que tome como argumento dos numeros y
devuelva el mayor de ellos.
"""

def max_de_tres(n1: int, n2: int, n3: int) -> int:
    """Dado tres numeros de entrada retornar el mayor

    Args:
        n1 (int): numero 1 a evaluar
        n2 (int): numero 2 a evaluar
        n3 (int): numero 3 a evaluar

    Returns:
        int: mayor de los tres
    """

    a = custom_max(n1, n2)
    b = custom_max(a, n3)
    return b

# print("Mayor de tres numeros")
print(max_de_tres(5,8,5), '\n')

"""
3 Definir una función reverse_list() donde dada una lista de elemetos
se inviertan los valores, no se puede utilizar la funcion reverse()
"""

def reverse_list(arr: list) -> list:
    """Devuelve una arr de n elemetos invertidos

    Args:
        arr (list): arr a invertir

    Returns:
        list: arr con elementos invertidos
    """

    # inicio = 0
    # fin = len(arr) - 1
    # while inicio < fin:
    #     arr[inicio], arr[fin] = arr[fin], arr[inicio]
    #     inicio += 1
    #     fin -= 1
    arr = arr[::-1]
    return arr

# lista = [1,2,3,4,5,6,7,8,9]
# print(f"Invertir lista \nLista original: {lista}")
# print(f"lista invertida: {reverse_list(lista)}\n")

"""
4 Definir una función insertion_sort() y ordenar una los elementos
de la lista
"""

def insertion_sort(arr: list):
    """Ordena los elemetos de una lista con el metodo insert sort

    Args:
        arr (list): lista a ordenar

    Returns:
        list: lista ordenada
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# lista = [19,32,1,87,43,17]
# print(f"Ordenar lista \nLista original {lista}")
# insertion_sort(lista)
# print(f"Lista ordenada {lista}\n")

"""
5 definir una funcion para eliminar los numero impares de lista_original
utilizando como apoyo lista_auxiliar la funcion debe ejecutarce en menos de 1 segundo
de la lista
"""

def eliminar_pares() -> time:
    lista_original = list(range(1, 1000001))
    lista_auxiliar = set(range(1, 1000001, 2))
    inicio = time.time()

    ####################
    # Escribe tu codigo
    ####################

    lista_nueva = [elemento for elemento in lista_original if elemento not in lista_auxiliar]

    ###################

    fin = time.time()
    tiempo = fin - inicio
    return tiempo, lista_nueva

tiempo, arr = eliminar_pares()
print(f"tiempo: {tiempo}")
#print(f"Lista impares: {arr}")



"""
6 Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def is_vocal(caracter: str) -> str:
    vocales = ['a', 'e', 'i', 'o', 'u']
    return True if caracter in vocales else False

# print(f"Es vocal: {is_vocal('a')}")
# print(f"Es vocal: {is_vocal('p')}")

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

# lista = [1, 2 ,3 ,4]
# sum(lista)
# multiplicacion(lista)

"""
8 Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena 
"estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def invertir_cadena(cadena: str) -> str:
    # cadena_invertida = cadena[::-1]
    cadena_lista = list(cadena)
    inicio = 0
    fin = len(cadena_lista) - 1

    while inicio < fin:
        cadena_lista[inicio], cadena_lista[fin] = cadena_lista[fin], cadena_lista[inicio]
        inicio += 1
        fin -= 1
    cadena_lista = ''.join(cadena_lista)
    return cadena_lista


# print(f"Invertir cadena \nCadena original: {'hola mundo'}")
# print(f"lista invertida: {invertir_cadena('hola mundo')}\n")


"""
9 - Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
def is_palindromo(cadena: str) -> bool:
    palimdromo = invertir_cadena(cadena)
    return True if palimdromo == cadena else False 
        

# print(f"Palabra: {'sometemos'}")
# print(f"Es palindromo: {is_palindromo('sometemos')}\n")


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

# print(f"tienen un elemento en comun: {superposicion(lista1, lista2)}")
# print(f"tienen un elemento en comun: {superposicion(lista1, lista3)}")

"""
11- Definir un histograma procedimiento() que tome una lista de números 
enteros e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******
"""

def histograma(arr: list):
    for i in arr:
        histograma = '*' * i
        print(histograma)

# histograma([4,8,6])


def numero_a_cadena(n: int) -> str:
    return str(n)

# print(f"Tipo de dato: {type(numero_a_cadena(7))}")

import re

"""
12- definir una funcion que reciba un string y lo convierta a minusculas
"""

def a_minusculas(cadena):
    return re.sub(r'[A-Z]', lambda x: chr(ord(x.group()) + 32), cadena)

def a_mayusculas(cadena):
    return re.sub(r'[a-z]', lambda x: chr(ord(x.group()) - 32), cadena)


"""
12- definir una funcion que reciba un string y sustituya las vocales por espacios 
y retorne el nuevo string
"""
def vocal_espacio(cadena: str) -> str:
    vocales = ['a', 'e', 'i', 'o', 'u']
    resultado = list(cadena)
    for i in range(len(resultado)):
        for j in range(len(vocales)):
            if resultado[i] == vocales[j]:
                resultado[i] = ' '
    resultado = ''.join(resultado)
    return resultado



"""
12- definir una funcion que reciba un string y sustituya las vocales de la siguiente manera
vocales = ['a', 'e', 'i', 'o', 'u']
caracter = ['x', '-', '+', '*', '&']
"""
def cambiar_vocal(cadena: str) -> str:
    vocales =  ['a', 'e', 'i', 'o', 'u']
    caracter = ['x', '-', '+', '*', '&']
    resultado = list(cadena)

    for i in range(len(resultado)):
        for j, k in zip(vocales,caracter):
            if resultado[i] == j:
                resultado[i] = k
    resultado = ''.join(resultado)

    return resultado

print("hola que tal mucho gusto esto es una prueba tecnica de python")
# print(vocal_espacio("hola que tal mucho gusto esto es una prueba tecnica de python"))
print(cambiar_vocal("hola que tal mucho gusto esto es una prueba tecnica de python"))