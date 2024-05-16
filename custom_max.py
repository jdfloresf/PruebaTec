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

print("Mayor de dos numeros")
print(custom_max(5,9), '\n')