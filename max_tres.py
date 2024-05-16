from custom_max import custom_max 
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
print(max_de_tres(9,8,5), '\n')