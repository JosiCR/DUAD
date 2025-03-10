lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = []

for num in lista:
    if num % 2 == 0:
        numeros_pares.append(num)
lista = numeros_pares
print(lista)