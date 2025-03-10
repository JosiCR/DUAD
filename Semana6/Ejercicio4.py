def sumar(lista):
    sum = 0
    for numeros in lista:
        sum += numeros
    return sum 


def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = sumar(lista)
    print('Lasuma de todos los numeros de la lista es:', resultado)


main()