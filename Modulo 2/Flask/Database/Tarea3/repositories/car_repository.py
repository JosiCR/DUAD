def get_cars(connection, filters):
    allowed_columns = [
        "id",
        "brand",
        "model",
        "manufacturing_year",
        "status"
    ]

    cursor = connection.cursor()

    query = """
        SELECT id, brand, model, manufacturing_year, status
        FROM lyfter_car_rental.cars
    """

    values = []

    if filters:
        conditions = []

        for column, value in filters.items():
            if column not in allowed_columns:
                cursor.close()
                return None, "Invalid filter column"

            conditions.append(f"{column} = %s")
            values.append(value)

        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, values)
    cars = cursor.fetchall()

    cursor.close()

    return cars, None


def create_car(connection, data):
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


def update_car_status(connection, car_id, status):
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lyfter_car_rental.cars
        SET status = %s
        WHERE id = %s
    """, (
        status,
        car_id
    ))

    connection.commit()
    cursor.close()


def get_car_status(connection, car_id):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT status
        FROM lyfter_car_rental.cars
        WHERE id = %s
    """, (car_id,))

    car = cursor.fetchone()

    cursor.close()

    return car


def set_car_status(connection, car_id, status):
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lyfter_car_rental.cars
        SET status = %s
        WHERE id = %s
    """, (
        status,
        car_id
    ))

    connection.commit()
    cursor.close()