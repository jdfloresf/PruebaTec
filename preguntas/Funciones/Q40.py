# 40. Write a Python function to reverse a string.

def invertir_cadena(cadena: str) -> str:
    cadena_invertida = cadena[::-1]
    return cadena_invertida

print(f"Invertir cadena \nCadena original: {'hola mundo'}")
print(f"lista invertida: {invertir_cadena('hola mundo')}\n")