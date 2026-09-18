CREATE TABLE lyfter_car_rental.users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    NAME VARCHAR(100),
    email VARCHAR(40) UNIQUE,
    username varchar(20) UNIQUE,
    password varchar(20),
    birth_date date 
    account_status varchar(20) DEFAULT "active"
);
