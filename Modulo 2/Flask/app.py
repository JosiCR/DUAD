from flask import Flask, request
import json

app = Flask(__name__)

def leer_tareas():
    with open("tareas.json", "r") as archivo:
        return json.load(archivo)


@app.route("/tareas", methods=["GET"])
def obtener_tareas():
    tareas = leer_tareas()
    estado = request.args.get("estado")

    if estado:
        tareas = [tarea for tarea in tareas if tarea["estado"] == estado]

    return tareas


@app.route("/tareas", methods=["POST"])
def crear_tarea():
    datos = request.get_json()

    tareas = leer_tareas()

    if not datos.get("titulo"):
        return "La tarea debe tener un título", 400

    if not datos.get("descripcion"):
        return "La tarea debe tener una descripción", 400

    if not datos.get("estado"):
        return "La tarea debe tener un estado", 400

    estados_validos = ["Por Hacer", "En Progreso", "Completada"]

    if datos["estado"] not in estados_validos:
        return "Estado inválido", 400

    for tarea in tareas:
        if tarea["id"] == datos["id"]:
            return "El identificador ya existe", 400

    tareas.append(datos)

    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo, indent=4)

    return datos, 201

@app.route("/tareas/<int:id>", methods=["PUT"])
def editar_tarea(id):
    tareas = leer_tareas()

    for tarea in tareas:
        if tarea["id"] == id:
            datos = request.get_json()

            if not datos.get("titulo"):
                return "La tarea debe tener un título", 400

            if not datos.get("descripcion"):
                return "La tarea debe tener una descripción", 400

            if not datos.get("estado"):
                return "La tarea debe tener un estado", 400

            estados_validos = ["Por Hacer", "En Progreso", "Completada"]

            if datos["estado"] not in estados_validos:
                return "Estado inválido", 400

            tarea["titulo"] = datos["titulo"]
            tarea["descripcion"] = datos["descripcion"]
            tarea["estado"] = datos["estado"]

            with open("tareas.json", "w") as archivo:
                json.dump(tareas, archivo, indent=4)

            return tarea, 200

    return "La tarea no existe", 404


@app.route("/tareas/<int:id>", methods=["DELETE"])
def eliminar_tarea(id):
    tareas = leer_tareas()

    for tarea in tareas:
        if tarea["id"] == id:
            tareas.remove(tarea)

            with open("tareas.json", "w") as archivo:
                json.dump(tareas, archivo, indent=4)

            return "Tarea eliminada correctamente", 200

    return "La tarea no existe", 404


@app.route("/")
def inicio():
    return "¡Mi API de tareas está funcionando!"
if __name__ == "__main__":
    app.run(debug=True)


