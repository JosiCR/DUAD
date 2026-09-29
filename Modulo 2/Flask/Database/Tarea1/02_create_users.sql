CREATE TABLE lyfter_car_rental.users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(40) UNIQUE,
    username VARCHAR(20) UNIQUE,
    password VARCHAR(20),
    birth_date DATE,
    account_status VARCHAR(20) DEFAULT 'Active'
);