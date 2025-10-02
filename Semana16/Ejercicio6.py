def contador_lower_upper(j):
    contador_mayuscula = 0
    contador_minuscula = 0
    for char in j:
        if char.isupper():
            contador_mayuscula += 1
        elif char.islower():
            contador_minuscula += 1
    return contador_mayuscula, contador_minuscula

    print(f"There’s {contador_mayuscula} upper cases and {contador_minuscula} lower cases")

contador_lower_upper("I also Love Nacion Sushi")