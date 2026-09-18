from flask import Flask, request, jsonify
import psycopg


app = Flask(__name__)


def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="YOUR_POSTGRES_PASSWORD"
    )
    return connection


@app.route("/")
def home():
    return "My car rental API is working!"


@app.route("/users")
def get_users():
    filters = request.args.to_dict()

    allowed_columns = [
        "id",
        "name",
        "email",
        "username",
        "password",
        "birth_date",
        "account_status"
    ]

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM lyfter_car_rental.users"
    values = []

    if filters:
        conditions = []

        for column, value in filters.items():
            if column not in allowed_columns:
                cursor.close()
                connection.close()
                return "Invalid filter column", 400

            conditions.append(f"{column} = %s")
            values.append(value)

        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, values)
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    result = []

    for user in users:
        result.append({
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "username": user[3],
            "password": user[4],
            "birth_date": str(user[5]),
            "account_status": user[6]
        })

    return jsonify(result)



@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO lyfter_car_rental.users (
            name,
            email,
            username,
            password,
            birth_date
        )
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data["name"],
        data["email"],
        data["username"],
        data["password"],
        data["birth_date"]
    ))

    connection.commit()

    cursor.close()
    connection.close()

    return "User created successfully!"


@app.route("/users/<int:user_id>/status", methods=["PUT"])
def update_user_status(user_id):
    data = request.get_json()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lyfter_car_rental.users
        SET account_status = %s
        WHERE id = %s
    """, (
        data["status"],
        user_id
    ))

    connection.commit()

    cursor.close()
    connection.close()

    return "User status updated successfully!"



@app.route("/users/<int:user_id>/delinquent", methods=["PUT"])
def flag_user_delinquent(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lyfter_car_rental.users
        SET account_status = 'Delinquent'
        WHERE id = %s
    """, (user_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return "User flagged as delinquent successfully!"


@app.route("/cars", methods=["POST"])
def create_car():
    data = request.get_json()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO lyfter_car_rental.cars (
            brand,
            model,
            manufacturing_year
        )
        VALUES (%s, %s, %s)
    """, (
        data["brand"],
        data["model"],
        data["manufacturing_year"]
    ))

    connection.commit()

    cursor.close()
    connection.close()

    return "Car created successfully!"

@app.route("/cars")
def get_cars():
    filters = request.args.to_dict()

    allowed_columns = [
        "id",
        "brand",
        "model",
        "manufacturing_year",
        "status"
    ]

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM lyfter_car_rental.cars"
    values = []

    if filters:
        conditions = []

        for column, value in filters.items():
            if column not in allowed_columns:
                cursor.close()
                connection.close()
                return "Invalid filter column", 400

            conditions.append(f"{column} = %s")
            values.append(value)

        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, values)
    cars = cursor.fetchall()

    cursor.close()
    connection.close()

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
def update_car_status(car_id):
    data = request.get_json()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lyfter_car_rental.cars
        SET status = %s
        WHERE id = %s
    """, (
        data["status"],
        car_id
    ))

    connection.commit()

    cursor.close()
    connection.close()

    return "Car status updated successfully!"



@app.route("/rentals", methods=["POST"])
def create_rental():
    data = request.get_json()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT status
        FROM lyfter_car_rental.cars
        WHERE id = %s
    """, (data["car_id"],))

    car = cursor.fetchone()

    if car is None:
        cursor.close()
        connection.close()
        return "Car not found", 404

    if car[0] != "Available":
        cursor.close()
        connection.close()
        return "Car is not available", 400

    cursor.execute("""
        INSERT INTO lyfter_car_rental.rentals (
            user_id,
            car_id
        )
        VALUES (%s, %s)
    """, (
        data["user_id"],
        data["car_id"]
    ))

    cursor.execute("""
        UPDATE lyfter_car_rental.cars
        SET status = 'Rented'
        WHERE id = %s
    """, (data["car_id"],))

    connection.commit()

    cursor.close()
    connection.close()

    return "Rental created successfully!"



@app.route("/rentals")
def get_rentals():
    filters = request.args.to_dict()

    allowed_columns = [
        "id",
        "user_id",
        "car_id",
        "rental_date",
        "status"
    ]

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM lyfter_car_rental.rentals"
    values = []

    if filters:
        conditions = []

        for column, value in filters.items():
            if column not in allowed_columns:
                cursor.close()
                connection.close()
                return "Invalid filter column", 400

            conditions.append(f"{column} = %s")
            values.append(value)

        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, values)
    rentals = cursor.fetchall()

    cursor.close()
    connection.close()

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
def complete_rental(rental_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT car_id
        FROM lyfter_car_rental.rentals
        WHERE id = %s
    """, (rental_id,))

    rental = cursor.fetchone()

    if rental is None:
        cursor.close()
        connection.close()
        return "Rental not found", 404

    car_id = rental[0]

    cursor.execute("""
        UPDATE lyfter_car_rental.rentals
        SET status = 'Completed'
        WHERE id = %s
    """, (rental_id,))

    cursor.execute("""
        UPDATE lyfter_car_rental.cars
        SET status = 'Available'
        WHERE id = %s
    """, (car_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return "Rental completed successfully!"



@app.route("/rentals/<int:rental_id>/status", methods=["PUT"])
def update_rental_status(rental_id):
    data = request.get_json()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lyfter_car_rental.rentals
        SET status = %s
        WHERE id = %s
    """, (
        data["status"],
        rental_id
    ))

    connection.commit()

    cursor.close()
    connection.close()

    return "Rental status updated successfully!"

if __name__ == "__main__":
    app.run(debug=True)