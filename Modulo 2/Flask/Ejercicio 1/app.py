from flask import Flask, request, jsonify
import json

app = Flask(__name__)

VALID_STATUSES = ["To Do", "In Progress", "Completed"]


def read_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)


def write_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def validate_task_data(data):
    if data is None:
        return "Request body must contain JSON data"

    if "id" not in data:
        return "Task must have an ID"

    if not data.get("title"):
        return "Task must have a title"

    if not data.get("description"):
        return "Task must have a description"

    if not data.get("status"):
        return "Task must have a status"

    if data["status"] not in VALID_STATUSES:
        return "Invalid status"

    return None


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = read_tasks()

    status = request.args.get("status")

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True)

    error = validate_task_data(data)

    if error:
        return jsonify({"error": error}), 400

    tasks = read_tasks()

    for task in tasks:
        if task["id"] == data["id"]:
            return jsonify({"error": "Task ID already exists"}), 400

    tasks.append(data)

    write_tasks(tasks)

    return jsonify(data), 201


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.get_json(silent=True)

    error = validate_task_data(data)

    if error:
        return jsonify({"error": error}), 400

    tasks = read_tasks()

    for task in tasks:
        if task["id"] == id:
            task["title"] = data["title"]
            task["description"] = data["description"]
            task["status"] = data["status"]

            write_tasks(tasks)

            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    tasks = read_tasks()

    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)

            write_tasks(tasks)

            return jsonify({"message": "Task deleted successfully"}), 200

    return jsonify({"error": "Task not found"}), 404


@app.route("/")
def home():
    return jsonify({"message": "My task API is working!"}), 200


if __name__ == "__main__":
    app.run(debug=True)