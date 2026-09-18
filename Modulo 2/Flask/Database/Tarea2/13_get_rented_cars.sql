SELECT cars.*
FROM lyfter_car_rental.cars
JOIN lyfter_car_rental.rentals
    ON cars.id = rentals.car_id
WHERE rentals.status = 'Active';

SELECT *
FROM lyfter_car_rental.cars
WHERE status = 'Available';