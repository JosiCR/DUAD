list_a = ['first_name', 'last_name', 'role']
list_b = [ 'Josias', 'Nunez', 'Operario']

dic_listas = {}

for combinar in range(len(list_a)):
    dic_listas[list_a[combinar]] = list_b[combinar]

print(dic_listas)