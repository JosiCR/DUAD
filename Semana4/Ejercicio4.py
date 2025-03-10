Total_de_notas = int(input("Ingrese la cantidad de notas"))
contador_notas = 1
cantidad_notas_aprobadas = 0
cantidad_notas_desaprobadas = 0
promedio_notas_aprobadas = 0
promedio_notas_desaprobadas = 0
promedio_notas_total = 0
while(contador_notas <= Total_de_notas):
    nota_actual = int(input(f'ingrese la nota numero {contador_notas}'))
    contador_notas += 1
    if (nota_actual < 70):
        cantidad_notas_desaprobadas =+ 1
        promedio_notas_desaprobadas =+ nota_actual
    else:
        cantidad_notas_aprobadas =+ 1
        promedio_notas_aprobadas =+ nota_actual
    promedio_notas_total = promedio_notas_total + nota_actual / Total_de_notas
promedio_notas_desaprobadas = promedio_notas_desaprobadas / cantidad_notas_desaprobadas
promedio_notas_aprobadas = promedio_notas_aprobadas / cantidad_notas_aprobadas

print(f'El estudiante tiene esta cantidad de notas aprobadas{cantidad_notas_aprobadas}')
print(f'Este es el promedio de notas aprobadas{promedio_notas_aprobadas}')
print(f'El estudiante tiene esta cantidad de notas desaprobadas{cantidad_notas_desaprobadas}')
print(f'Este es el promedio de notas desaprobadas{promedio_notas_desaprobadas}')
print(f'este es el promedio total de notas{promedio_notas_total}')