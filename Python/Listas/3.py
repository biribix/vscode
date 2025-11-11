n = int(input("¿Cuántos elementos tienen los vectores?: "))
print()

vector1 = []
vector2 = []
producto_escalar = 0

print(f"Ingresa los {n} elementos del primer vector: ")
for i in range(n):
    v1 = float(input(f"Elemento {i+1}: "))
    vector1.append(v1)
print()

print(f"Ingresa los {n} elementos del segundo vector:")
for i in range(n):
    v2 = float(input(f"Elemento {i+1}: "))
    vector2.append(v2)
print()

for i in range(n):
    producto_escalar += vector1[i] * vector2[i]
print()

print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")
print()
print(f"Producto escalar: {producto_escalar}")
