from sqlalchemy.orm import Session

from database import engine
from models import Base
from user_manager import UserManager
from car_manager import CarManager
from address_manager import AddressManager


Base.metadata.create_all(engine)


with Session(engine) as session:
    user_manager = UserManager(session)
    car_manager = CarManager(session)
    address_manager = AddressManager(session)

    # Create User
    user = user_manager.create_user(
        name="Carlos",
        email="carlos@email.com"
    )

    print(f"Created user: {user.id} - {user.name} - {user.email}")

    # Get All Users
    users = user_manager.get_all_users()

    for user in users:
        print(user.id, user.name, user.email)

    # Create Car
    car = car_manager.create_car(
        brand="Toyota",
        model="Corolla"
    )

    print(f"Created car: {car.id} - {car.brand} - {car.model}")

    # Assign Car to User
    car_manager.assign_car_to_user(
        car_id=car.id,
        user_id=user.id
    )

    # Create Address
    address = address_manager.create_address(
        address="Heredia, Costa Rica",
        user_id=user.id
    )

    print(f"Created address: {address.id} - {address.address}")