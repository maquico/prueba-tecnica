def detectar_palindromo(palabra):
    palabra_invertida = palabra[::-1]
    return True if palabra == palabra_invertida else False

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    print("Es palindromo") if detectar_palindromo(palabra) else print("No es palindromo")