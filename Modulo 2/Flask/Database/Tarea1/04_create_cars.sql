Create TABLE lyfter_car_rental.cars (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    brand VARCHAR(30),
    model VARCHAR(30),
    manufacturing_year INTEGER,
    status VARCHAR(15) DEFAULT 'Available'
);