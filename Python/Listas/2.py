palabra = input("Ingresa una palabra: ")

palabra_limpia = palabra.lower().replace(" ", "")
    
if palabra_limpia == palabra_limpia[::-1]:
    print(f"✓ '{palabra}' SÍ es un palíndromo\n")
else:
    print(f"✗ '{palabra}' NO es un palíndromo\n")
