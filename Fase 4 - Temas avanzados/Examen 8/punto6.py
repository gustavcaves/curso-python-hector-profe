# Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo valor es igual a su índice. Utilizar la función enumerate.

# Forma 1
lista = [0, 1, 3, 4, 5, 6, 7]

def rCantidadElementos(lista):
    listavacia = []
    for k,v in enumerate(lista):
        if v==k:
            listavacia.append(v)
    return len(listavacia)

print(rCantidadElementos(lista))

# Forma 2
def rCantidadElementos2(L):
    return len([v for k,v in enumerate(L) if v==k])

print(rCantidadElementos2(lista))