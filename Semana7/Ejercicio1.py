def calculator():
    try:
        current_number = float(input("Ingrese el numero inicial: "))

        while True:
            print(f"\nNumero actual: {current_number}")
            print("Menu")
            print("1- Suma")
            print("2- Resta")
            print("3- Multiplicacion")
            print("4- Division")
            print("5- Borrar Resultado")
            print("6- Salir")

            option = input("seleccione la opcion que desea ejecutar: ")

            if option not in ["1", "2", "3", "4", "5", "6"]:
                raise ValueError("opcion invalida. Por favor, elija un numero entre 1 y 6.")
            
            if option == "6":
                print("¡Espero y te haya funcionado!")
                break

            if option == "5":
                current_number = float(input("Ingrese el nuevo numero inicial: "))
                print("El resultado fue borrado")
                continue

            try:
                new_number = float(input("Ingrese el numero con el que desea operar: "))
            except ValueError:
                raise ValueError("Numero invalido. Debe ingresar un numero valido.")

            print(f"operando con el numero: {new_number}")
            
            if option == "1":
                current_number += new_number
            elif option =="2":
                current_number -= new_number
            elif option == "3":
                current_number *= new_number
            elif option == "4":
                if new_number == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero.")
                current_number /= new_number

            print(f"Resultado: {current_number}")

    except ValueError as error:
        print(f"Error: {error}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"error no identificado: {error}")


calculator()