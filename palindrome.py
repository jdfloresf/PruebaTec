from inversa import invertir_cadena
"""
9 - Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
def is_palindromo(cadena: str) -> bool:
    palimdromo = invertir_cadena(cadena)
    return True if palimdromo == cadena else False 
        

print(f"Palabra: {'sometemos'}")
print(f"Es palindromo: {is_palindromo('sometemos')}\n")