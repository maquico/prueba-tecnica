def detectar_palindromo(palabra):
    palabra_invertida = palabra[::-1]
    return True if palabra == palabra_invertida else False
        