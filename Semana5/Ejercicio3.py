lista = [1, 2, 3, 4, 5, 6, 7]
if len(lista) > 1 :
    lista[0], lista[-1] = lista[-1], lista[0]
print(lista)