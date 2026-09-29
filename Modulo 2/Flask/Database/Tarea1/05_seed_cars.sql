INSERT INTO lyfter_car_rental.cars (
    brand,
    model,
    manufacturing_year,
    status
)
SELECT
    'Toyota' AS brand,
    'Corolla ' || number AS model,
    2025 AS manufacturing_year,
    'Available' AS status
FROM generate_series(1, 50) AS number;