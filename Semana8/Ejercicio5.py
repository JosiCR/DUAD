import json

file_path = r"C:/Users/josia/Downloads/pokemon.json"

def read_pokemon():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return[]
    

def save_pokemon(list_pokemon):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(list_pokemon, file, indent=2, ensure_ascii=False)


def add_pokemon():
    list_pokemon = read_pokemon()

    print("\nIngrese los datos del nuevo pokemon:")
    name = input("Nombre: ")
    tipo = input("Tipo (si es mas de uno, separar con coma): ").split(",")
    tipo = [t.strip() for t in tipo]

    hp = int(input("HP: "))
    Attack = int(input("Attack: "))
    Defense= int(input("Defense: "))
    SP_Attack = int(input("Sp. Attack: "))
    SP_Defense = int(input("Sp. Defense: "))
    Speed = int(input("Speed: "))


    new_pokemon = {
        "name": {"english": name},
        "type": tipo,
        "base": {
            "HP": hp,
            "Attack": Attack,
            "Defense": Defense,
            "Sp. Attack": SP_Attack,
            "Sp. Defense": SP_Defense,
            "Speed": Speed
        }
    }

    list_pokemon = list_pokemon + [new_pokemon]
    save_pokemon(list_pokemon)

    print(f"\n El pokemon {name} ha sido agregado al archivo")

add_pokemon()