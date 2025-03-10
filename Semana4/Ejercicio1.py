Nombre = input("Ingrese su nombre:")
apellido = input ("Ingrese su apellido:")
edad = (int(input(" Ingrese su edad:")))

if (edad <= 2 ):
    print("Usted es un bebe")
elif (edad <= 9):
    print("Usted es un niño")
elif (edad <= 13):
    print("Usted es un pre adolescente")
elif (edad <= 18):
    print("Usted es un adolescente")
elif (edad <= 29):
    print("Usted es un adulto joven")
elif (edad <= 59):
    print("Usted es un adulto")
elif (edad >= 60):
    print("Usted es un adulto mayor")