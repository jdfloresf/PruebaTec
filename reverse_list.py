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

lista = [1,2,3,4,5,6,7,8,9]
print(f"Invertir lista \nLista original: {lista}")
print(f"lista invertida: {reverse_list(lista)}\n")