import csv

def input_videogames():
    
    file_path = r"C:\Users\josia\Downloads\videojuegos.tsv"

    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        fields = ['nombre', 'genero', 'desarrollador', 'clasificacion']
        writer = csv.DictWriter(file, delimiter="\t", fieldnames=fields)

        writer.writeheader()

        n = int(input("cuantos videojuegos desea ingresar?"))

        for i in range(n):
            print(f"\nIngrese los datos para el juego #{i + 1}:")
            nombre = input("Nombre: ")
            genero = input("Genero: ")
            desarrollador = input("Desarrollador: ")
            clasificacion = input("Clasificacion ESRB: ")

            writer.writerow({
                'nombre': nombre,
                'genero': genero,
                'desarrollador': desarrollador,
                'clasificacion': clasificacion
            })

    print("\nLos videojuegos se guardaron en 'videojuegos.tsv'.")

input_videogames()