def get_rentals(connection, filters):
    allowed_columns = [
        "id",
        "user_id",
        "car_id",
        "rental_date",
        "status"
    ]

    cursor = connection.cursor()

    query = """
        SELECT id, user_id, car_id, rental_date, status
        FROM lyfter_car_rental.rentals
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
    rentals = cursor.fetchall()

    cursor.close()

    return rentals, None


def create_rental(connection, user_id, car_id):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO lyfter_car_rental.rentals (
            user_id,
            car_id
        )
        VALUES (%s, %s)
    """, (
        user_id,
        car_id
    ))

    cursor.execute("""
        UPDATE lyfter_car_rental.cars
        SET status = 'Rented'
        WHERE id = %s
    """, (car_id,))

    connection.commit()
    cursor.close()


def get_rental_car(connection, rental_id):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT car_id
        FROM lyfter_car_rental.rentals
        WHERE id = %s
    """, (rental_id,))

    rental = cursor.fetchone()

    cursor.close()

    return rental


def complete_rental(connection, rental_id, car_id):
    cursor = connection.cursor()

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


def update_rental_status(connection, rental_id, status):
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lyfter_car_rental.rentals
        SET status = %s
        WHERE id = %s
    """, (
        status,
        rental_id
    ))

    connection.commit()
    cursor.close()