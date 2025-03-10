num1 = int(input("Por favor ingrese el primer numero"))
num2 = int(input("Por favor ingrese el segundo numero"))
num3 = int(input("Por favor ingrese el tercer numero"))
if (num1 > num2 and num1 > num3):
    print(f'El numero mayor es {num1}')
elif (num2 > num1 and num2 > num3):
    print(f'El numero mayor es {num2}')
else:
    print(f'El numero mayor es {num3}')