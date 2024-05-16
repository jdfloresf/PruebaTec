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
lista = [19,32,1,87,43,17]
print(f"Ordenar lista \nLista original {lista}")
insertion_sort(lista)
print(f"Lista ordenada {lista}\n")