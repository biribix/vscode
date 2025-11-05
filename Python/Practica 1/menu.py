# Programa de calculo de circunferencias con el radio
# Hecho por David Abad Martínez de 2ºSMR A

# Número de errores cometidos
error = 0

# Activación del bucle
continuar = True

# Menú de opciones
menu = "------------------------------------------------------------------------------\n" \
    "                                 CALCULADORA\n" \
    "------------------------------------------------------------------------------\n" \
    "1. Cálculo del perimetro de una circunferencia\n" \
    "2. Cálculo del area de un circulo\n" \
    "3. Cálculo del volumen de una esfera\n" \
    "4. Salir\n" \
    "------------------------------------------------------------------------------"

while continuar:
    print(menu)
    opcion = int(input("Elige una de estas opciones (1-4): "))
    print()

    if ( opcion == 1 ):
        radio = float(input("Introduzca el valor del radio: "))
        perimetro = 2 * 3.1416 * radio                                   # Operación para calcular el perimetro de una circunferencia: P=2*π*r
        print("El perimetro de la circunferencia es:",perimetro,"cm\n")  # Resultado
            

    elif ( opcion == 2 ):
        radio = float(input("Introduzca el valor del radio: "))
        area = radio ** 2 * 3.1416                                       # Operación para calcular el area de un circulo: A=r²*π
        print("El area de la circunferencia es:",area,"cm²\n")           # Resultado

    elif ( opcion == 3 ):
        radio = float(input("Introduzca el valor del radio: "))
        volumen = (4 / 3) * 3.1416 * radio ** 3                          # Operación para calcular el volumen de una esfera: V=(4/3)*π*r³
        print("El volumen de la esfera es:",volumen,"cm³\n")             # Resultado

    elif ( opcion == 4 ):
        continuar = False

    else:
        error = error + 1
        print("ERROR",error,": Opción no valida, elige una opción entre el 1 y el 4.\n")

print("FIN DEL PROGRAMA\n")