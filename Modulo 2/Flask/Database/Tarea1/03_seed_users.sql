INSERT INTO lyfter_car_rental.users (
    name,
    email,
    username,
    password,
    birth_date,
    account_status
)
SELECT
    'User ' || number AS name,
    'user' || number || '@example.com' AS email,
    'user' || number AS username,
    'password' || number AS password,
    '2004-12-14'::DATE AS birth_date,
    'Active' AS account_status
FROM generate_series(1, 50) AS number;