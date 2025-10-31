contraseña = "password1234"
palabra = input("Introduce la contraseña: ")

while not palabra == contraseña:
    print("Contraseña icorrecta")
    palabra = input("Introduce la contrasela correcta: ")

print("Contraseña correcta, bienvenido")