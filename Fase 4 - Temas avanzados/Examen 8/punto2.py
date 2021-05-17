# Crear una función que tome un listado de dígitos y devuelva al número al
# que corresponden.
# Por ejemplo [1,2,3] corresponde al número ciento veintitrés (123). Utilizar
# la función reduce.

from functools import reduce

digitos = [1, 2, 3]

def numero(listado):
    return reduce(lambda x,y:x*10 + y,listado)

print(numero(digitos))