numero_secreto = 9
Respuesta = int(input("Adivine el numero secreto del 1 al 10"))

while(Respuesta != numero_secreto):
    print("Numero incorrecto por favor intentalo de nuevo")
    Respuesta = int(input("Adivine el numero secreto del 1 al 10"))
print("Felicidades el numero secreto era 9 ")