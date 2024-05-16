"""
 definir una funcion que reciba un string y sustituya las vocales por espacios 
y retorne el nuevo string
"""
# def vocal_espacio(cadena: str) -> str:
#     vocales = ['a', 'e', 'i', 'o', 'u']
#     resultado = list(cadena)
#     for i in range(len(resultado)):
#         for j in range(len(vocales)):
#             if resultado[i] == vocales[j]:
#                 resultado[i] = ' '
#     resultado = ''.join(resultado)
#     return resultado
def vocal_espacio(cadena: str) -> str:
    vocales = ['a', 'e', 'i', 'o', 'u']
    return ''.join([' ' if c in vocales else c for c in cadena])




"""
definir una funcion que reciba un string y sustituya las vocales de la siguiente manera
vocales = ['a', 'e', 'i', 'o', 'u']
caracter = ['x', '-', '+', '*', '&']
"""
# def cambiar_vocal(cadena: str) -> str:
#     vocales =  ['a', 'e', 'i', 'o', 'u']
#     caracter = ['x', '-', '+', '*', '&']
#     resultado = list(cadena)

#     for i in range(len(resultado)):
#         for j, k in zip(vocales,caracter):
#             if resultado[i] == j:
#                 resultado[i] = k
#     resultado = ''.join(resultado)
#     return resultado

def cambiar_vocal(cadena: str) -> str:
    vocales = ['a', 'e', 'i', 'o', 'u']
    character = ['x', '-', '+', '*', '&']

    return "".join([character[vocales.index(c)] if c in vocales else c for c in cadena])



print("this is a test for python language")
print(vocal_espacio("this is a test for python language"))
print(cambiar_vocal("this is a test for python language"))