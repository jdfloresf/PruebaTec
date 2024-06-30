# Leer y procesar la entrada
n, m = (int(x) for x in input().split())
arr = [int(x) for x in input().split()]
A = {int(x) for x in input().split()}
B = {int(x) for x in input().split()}

# Inicializar la felicidad
happiness = 0

# Iterar sobre la lista de enteros
for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

# Imprimir el resultado final
print(happiness)
