
# Utilizar la función incorporada map() para crear una función que retorne
# una lista con la longitud de cada palabra (separas por espacios) de una
# frase. La función recibe una cadena de texto y retornara una lista.

frase = "Aprender a programar requiere tiempo y dedicación"

# Forma 1
def longitudPalabra(lista):
    lista2 = []
    lista3 = lista.split()
    for i in lista3:
        a = len(i)
        lista2.append(a)
    return lista2

print(longitudPalabra(frase))

# Forma 2
def lpalabras(frase):
    return list(map(len, frase.split()))
    
print(lpalabras(frase))

# Forma 3 
fl = lambda x: list(map(len, x.split()))
print(fl(frase))