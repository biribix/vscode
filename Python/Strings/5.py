dni = int(input("Introduce los números del DNI: "))

if len(int(dni)) == 8:
    resto = dni % 23

else:
    print("DNI no valido")