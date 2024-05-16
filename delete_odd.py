import time

"""
5 definir una funcion para eliminar los numero impares de lista_original
utilizando como apoyo lista_auxiliar la funcion debe ejecutarce en menos de 1 segundo
de la lista
"""

def delete_odd() -> time:
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

tiempo, arr = delete_odd()
print(f"tiempo: {tiempo}")