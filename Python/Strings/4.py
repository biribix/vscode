palabra = input("Introduce una palabra o frase: ")
contador = 0
for i in palabra.split():
    contador = contador + 1
print("Número de palabras: ",contador)
print("Número de carácteres:",len(palabra))