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

histograma([4,8,6])