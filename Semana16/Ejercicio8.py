def numero_primo(num):
    if num <= 1:
        return False
    for j in range (2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True


def separar_primos(lista):
    num_primos = []

    for num in lista:
        if numero_primo(num):
            num_primos.append(num)
    return num_primos


numeros = [1, 4, 6, 7, 13, 9, 67]
result = separar_primos(numeros)
print(result)