from flask import Flask, request, jsonify
import psycopg

from repositories.user_repository import (
    get_users,
    create_user,
    update_user_status,
    flag_user_delinquent
)

from repositories.car_repository import (
    get_cars,
    create_car,
    update_car_status,
    get_car_status
)

from repositories.rental_repository import (
    get_rentals,
    create_rental,
    get_rental_car,
    complete_rental,
    update_rental_status
)


app = Flask(__name__)


def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="JosiCR_14"
    )
    return connection


@app.route("/")
def home():
    return "My car rental API is working!"


@app.route("/users")
def list_users():
    filters = request.args.to_dict()

    connection = get_connection()

    users, error = get_users(connection, filters)

    connection.close()

    if error:
        return error, 400

    result = []

    for user in users:
        result.append({
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "username": user[3],
            "birth_date": str(user[4]),
            "account_status": user[5]
        })

    return jsonify(result)


@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    connection = get_connection()

    create_user(connection, data)

    connection.close()

    return "User created successfully!", 201


@app.route("/users/<int:user_id>/status", methods=["PUT"])
def change_user_status(user_id):
    data = request.get_json()

    connection = get_connection()

    update_user_status(
        connection,
        user_id,
        data["status"]
    )

    connection.close()

    return "User status updated successfully!"


@app.route("/users/<int:user_id>/delinquent", methods=["PUT"])
def flag_delinquent(user_id):
    connection = get_connection()

    flag_user_delinquent(connection, user_id)

    connection.close()

    return "User flagged as delinquent successfully!"


@app.route("/cars", methods=["POST"])
def add_car():
    data = request.get_json()

    connection = get_connection()

    create_car(connection, data)

    connection.close()

    return "Car created successfully!", 201


@app.route("/cars")
def list_cars():
    filters = request.args.to_dict()

    connection = get_connection()

    cars, error = get_cars(connection, filters)

    connection.close()

    if error:
        return error, 400

    result = []

    for car in cars:
        result.append({
            "id": car[0],
            "brand": car[1],
            "model": car[2],
            "manufacturing_year": car[3],
            "status": car[4]
        })

    return jsonify(result)


@app.route("/cars/<int:car_id>/status", methods=["PUT"])
def change_car_status(car_id):
    data = request.get_json()

    connection = get_connection()

    update_car_status(
        connection,
        car_id,
        data["status"]
    )

    connection.close()

    return "Car status updated successfully!"


@app.route("/rentals", methods=["POST"])
def add_rental():
    data = request.get_json()

    connection = get_connection()

    car = get_car_status(
        connection,
        data["car_id"]
    )

    if car is None:
        connection.close()
        return "Car not found", 404

    if car[0] != "Available":
        connection.close()
        return "Car is not available", 400

    create_rental(
        connection,
        data["user_id"],
        data["car_id"]
    )

    connection.close()

    return "Rental created successfully!", 201


@app.route("/rentals")
def list_rentals():
    filters = request.args.to_dict()

    connection = get_connection()

    rentals, error = get_rentals(connection, filters)

    connection.close()

    if error:
        return error, 400

    result = []

    for rental in rentals:
        result.append({
            "id": rental[0],
            "user_id": rental[1],
            "car_id": rental[2],
            "rental_date": str(rental[3]),
            "status": rental[4]
        })

    return jsonify(result)


@app.route("/rentals/<int:rental_id>/complete", methods=["PUT"])
def finish_rental(rental_id):
    connection = get_connection()

    rental = get_rental_car(
        connection,
        rental_id
    )

    if rental is None:
        connection.close()
        return "Rental not found", 404

    car_id = rental[0]

    complete_rental(
        connection,
        rental_id,
        car_id
    )

    connection.close()

    return "Rental completed successfully!"


@app.route("/rentals/<int:rental_id>/status", methods=["PUT"])
def change_rental_status(rental_id):
    data = request.get_json()

    connection = get_connection()

    update_rental_status(
        connection,
        rental_id,
        data["status"]
    )

    connection.close()

    return "Rental status updated successfully!"


if __name__ == "__main__":
    app.run(debug=True)