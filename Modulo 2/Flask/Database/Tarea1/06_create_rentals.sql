CREATE TABLE lyfter_car_rental.rentals (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INTEGER REFERENCES lyfter_car_rental.users(id),
    car_id INTEGER REFERENCES lyfter_car_rental.cars(id),
    rental_date DATE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(15) DEFAULT 'Active'
);
INSERT INTO lyfter_car_rental.rentals (
    user_id,
    car_id
)
VALUES (
    1,
    1
);