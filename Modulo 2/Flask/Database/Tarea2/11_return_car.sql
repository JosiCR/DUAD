UPDATE lyfter_car_rental.rentals
SET status = 'Completed'
WHERE id = 1;

UPDATE lyfter_car_rental.cars
SET status = 'Available'
WHERE id = 51;