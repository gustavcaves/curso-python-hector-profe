def palindromo(palabra):
    """
    Comprueba si una palabra es un palíndrimo, si lo es devuelve True y si no False
    Los palíndromos son palabras o frases que se leen igual de izquierda a derecha que de derecha a izquierda.
    
    >>> palindromo("radar")
    True

    >>> palindromo("somos")
    True

    >>> palindromo("Holah")
    False

    >>> palindromo("Ana")
    True

    >>> palindromo("Atar a la rata")
    True

    """
    if palabra.lower().replace(" ","") == palabra[::-1].lower().replace(" ",""): 
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()