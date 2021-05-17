# Crear una función que retorne las palabras de una lista de palabras que
# comience con una letra en específico. Utilizar la función filter.

lpalabras = ["maria", "hogar", "familia", "marte", "andromeda"]

def selecpalabras(lista, letra):
    return list(filter( lambda palabra: palabra[0]==letra, lista ))

print(selecpalabras(lpalabras,"m"))
