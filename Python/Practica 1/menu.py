# Programa de calculo de circunferencias con el radio
# Hecho por David Abad Martínez de 2ºSMR A

# Número pi
pi = 3.1416

# Número de errores cometidos
error = 0

# Menú de opciones
menu ="------------------------------------------------------------------------------\n" \
    "                                 CALCULADORA\n" \
    "------------------------------------------------------------------------------\n" \
    "1. Cálculo del perimetro de una circunferencia\n" \
    "2. Cálculo del area de un circulo\n" \
    "3. Cálculo del volumen de una esfera\n" \
    "4. Salir\n" \
    "------------------------------------------------------------------------------"

print(menu)
opcion = int(input("Elige una de estas opciones (1-4): "))
print()

# Mientras la opcion elegida sea una entre el 1 y el 4, 
while ( opcion == 1,2,3,4 ):

    # Opción 1: Cálculo del perimetro de una circunferencia
    if opcion == 1:
        print("------------------------------------------------------------------------------\n"
            "Cálculo del perímetro de una circunferencia\n"
            "------------------------------------------------------------------------------")
        radio = float(input("Introduzca el valor del radio: "))         # Valor del radio del circulo definido por el usuario
        perimetro = 2 * pi * radio                                      # Operación para calcular el perimetro de una circunferencia: P=2*π*r
        print("El perimetro de la circunferencia es:",perimetro,"cm\n"  # Resultado
            "------------------------------------------------------------------------------\n")
        print(menu)
        opcion = int(input("Elige una de estas opciones (1-4): "))
        print()

    # Opción 2: Cálculo del area de un circulo
    elif opcion == 2:
        print("------------------------------------------------------------------------------\n"
            "Cálculo del area de un circulo\n"
            "------------------------------------------------------------------------------")
        radio = float(input("Introduzca el valor del radio: "))         # Valor del radio del circulo definido por el usuario
        area = radio ** 2 * pi                                          # Operación para calcular el area de un circulo: A=r²*π
        print("El area de la circunferencia es:",area,"cm²\n"           # Resultado
            "------------------------------------------------------------------------------\n")
        print(menu)
        opcion = int(input("Elige una de estas opciones (1-4): "))
        print()

    # Opción 3: Cálculo del volumen de una esfera
    elif opcion == 3:
        print("------------------------------------------------------------------------------\n"
            "Cálculo del volumen de una esfera\n"
            "------------------------------------------------------------------------------")
        radio = float(input("Introduzca el valor del radio: "))         # Valor del radio del circulo definido por el usuario
        volumen = (4 / 3) * pi * radio ** 3                             # Operación para calcular el volumen de una esfera: V=(4/3)*π*r³
        print("El volumen de la esfera es:",volumen,"cm³\n"             # Resultado
            "------------------------------------------------------------------------------\n")
        print(menu)
        opcion = int(input("Elige una de estas opciones (1-4): "))
        print()

    # Opción 4: Salir
    elif opcion == 4:
        break
    
    # Si la opcion elegida no es una entre el 1 y el 4, da error y se vuelve a iniciar el programa
    else:
        error = error + 1
        print("* ERROR",error,": Opcion no valida\n")                   # Mensaje de error
        print(menu)
        opcion = int(input("Elige una de estas opciones (1-4): "))
        print()

print("FIN DEL PROGRAMA\n")
