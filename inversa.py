"""
8 Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena 
"estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def invertir_cadena(cadena: str) -> str:
    cadena_invertida = cadena[::-1]
    # cadena_lista = list(cadena)
    # inicio = 0
    # fin = len(cadena_lista) - 1

    # while inicio < fin:
    #     cadena_lista[inicio], cadena_lista[fin] = cadena_lista[fin], cadena_lista[inicio]
    #     inicio += 1
    #     fin -= 1
    # cadena_lista = ''.join(cadena_lista)
    return cadena_invertida


print(f"Invertir cadena \nCadena original: {'hola mundo'}")
print(f"lista invertida: {invertir_cadena('hola mundo')}\n")