import itertools

# Leer la entrada
N = int(input())
letters = input().split()
K = int(input())

# Generar todas las combinaciones de K elementos de la lista de letras
combinations = list(itertools.combinations(letters, K))
print(combinations)

# Contar las combinaciones que contienen al menos una 'a'
count = sum(1 for combo in combinations if 'a' in combo)
print(f"convinaciones con a {count}")
print(f"total de convinaciones: {len(combinations)}")
# Calcular la probabilidad
probability = count / len(combinations)

# Imprimir el resultado con tres decimales
print(f"{probability:.3f}")
