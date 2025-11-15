matematicas = float(input("Ingresa la nota de Matemáticas: "))
historia = float(input("Ingresa la nota de Historia: "))
ingles = float(input("Ingresa la nota de Inglés: "))
programacion = float(input("Ingresa la nota de Programación: "))
print()

suspendidas = []

if matematicas < 5:
    suspendidas.append("Matemáticas")
if historia < 5:
    suspendidas.append("Historia")
if ingles < 5:
    suspendidas.append("Inglés")
if programacion < 5:
    suspendidas.append("Programación")

# Mostrar resultado
if len(suspendidas) == 0:
    print("Has aprobado todas las asignaturas.")
else:
    print(f"Has suspendido {len(suspendidas)} asignatura(s):")
    for asignatura in suspendidas:
        print(f"  - {asignatura}")
