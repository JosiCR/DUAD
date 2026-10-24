def get_users(connection, filters):
    allowed_columns = [
        "id",
        "name",
        "email",
        "username",
        "password",
        "birth_date",
        "account_status"
    ]

    cursor = connection.cursor()

    query = """
        SELECT id, name, email, username, birth_date, account_status
        FROM lyfter_car_rental.users
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
    users = cursor.fetchall()

    cursor.close()

    return users, None


def create_user(connection, data):
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


def update_user_status(connection, user_id, status):
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lyfter_car_rental.users
        SET account_status = %s
        WHERE id = %s
    """, (
        status,
        user_id
    ))

    connection.commit()
    cursor.close()


def flag_user_delinquent(connection, user_id):
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lyfter_car_rental.users
        SET account_status = 'Delinquent'
        WHERE id = %s
    """, (user_id,))

    connection.commit()
    cursor.close()