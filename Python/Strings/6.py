def cifrado_cesar(texto, clave):
    """Cifra un texto usando el método del código César."""
    texto_cifrado = ""
    for letra in texto:
        # Verifica si la letra es mayúscula
        if letra.isupper():
            # Calcula el nuevo índice de la letra con el desplazamiento, 
            # ajustándolo al rango del abecedario (0-25) y convirtiéndolo a mayúscula
            letra_cifrada = chr((ord(letra) - ord('A') + clave) % 26 + ord('A'))
            texto_cifrado += letra_cifrada
        # Verifica si la letra es minúscula
        elif letra.islower():
            # Calcula el nuevo índice de la letra con el desplazamiento, 
            # ajustándolo al rango del abecedario (0-25) y convirtiéndolo a minúscula
            letra_cifrada = chr((ord(letra) - ord('a') + clave) % 26 + ord('a'))
            texto_cifrado += letra_cifrada
        # Si no es una letra (ej. espacio, número, puntuación), la deja igual
        else:
            texto_cifrado += letra
    return texto_cifrado

# 1. Pedir la frase al usuario
frase = input("Introduce la frase a cifrar: ")

# 2. Pedir la clave numérica (desplazamiento) al usuario
while True:
    try:
        clave = int(input("Introduce el número de la clave (un entero): "))
        break
    except ValueError:
        print("Por favor, introduce un número entero válido para la clave.")

# 3. Cifrar la frase y mostrar el resultado
frase_cifrada = cifrado_cesar(frase, clave)
print("La frase cifrada es:", frase_cifrada)
