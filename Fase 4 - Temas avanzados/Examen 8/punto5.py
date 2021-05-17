# Realizar una función que tome una lista y retorne un diccionario que contenga los valores de la lista como clave y el índice como el valor. Utilizar la función enumerate

lista = [1, 2, 3, 4, 5]

def listToDictionary(lista):
    # a = {k:v for v,k in enumerate(lista)}
    # print(a)
    return {k:v for v,k in enumerate(lista)}

print(listToDictionary(lista))

