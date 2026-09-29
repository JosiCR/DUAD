from sqlalchemy import select

from models import Car, User


class CarManager:
    def __init__(self, session):
        self.session = session

    def create_car(self, brand, model):
        car = Car(
            brand=brand,
            model=model
        )

        self.session.add(car)
        self.session.commit()
        self.session.refresh(car)

        return car

    def update_car(self, car_id, brand=None, model=None):
        statement = select(Car).where(Car.id == car_id)
        car = self.session.scalars(statement).first()

        if car is None:
            return None

        if brand is not None:
            car.brand = brand

        if model is not None:
            car.model = model

        self.session.commit()
        self.session.refresh(car)

        return car

    def delete_car(self, car_id):
        statement = select(Car).where(Car.id == car_id)
        car = self.session.scalars(statement).first()

        if car is None:
            return False

        self.session.delete(car)
        self.session.commit()

        return True

    def assign_car_to_user(self, car_id, user_id):
        car_statement = select(Car).where(Car.id == car_id)
        car = self.session.scalars(car_statement).first()

        user_statement = select(User).where(User.id == user_id)
        user = self.session.scalars(user_statement).first()

        if car is None or user is None:
            return False

        car.user = user

        self.session.commit()
        self.session.refresh(car)

        return True

    def get_all_cars(self):
        statement = select(Car)
        return self.session.scalars(statement).all()