numeros = []
for index in range(10):
    num = int(input(f"ingrese el numero{index + 1}:"))
    numeros.append(num)
numero_mayor = max(numeros)

print("numeros ingresados:", numeros, "numero mas alto ingresado" , numero_mayor)