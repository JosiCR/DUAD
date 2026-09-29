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

    print("\n=== USERS ===")

    users = user_manager.get_all_users()

    for user in users:
        print(user.id, user.name, user.email)

    print("\n=== CARS ===")

    cars = car_manager.get_all_cars()

    for car in cars:
        print(car.id, car.brand, car.model, car.user_id)

    print("\n=== ADDRESSES ===")

    addresses = address_manager.get_all_addresses()

    for address in addresses:
        print(address.id, address.address, address.user_id)

    # Create a test user
    test_user = user_manager.create_user(
        name="Test User",
        email="test.user@orm.com"
    )

    print("\n=== CREATED USER ===")
    print(test_user.id, test_user.name, test_user.email)

    # Update the test user
    updated_user = user_manager.update_user(
        user_id=test_user.id,
        name="Updated Test User"
    )

    print("\n=== UPDATED USER ===")
    print(updated_user.id, updated_user.name, updated_user.email)

    # Create a test car
    test_car = car_manager.create_car(
        brand="Toyota",
        model="Corolla"
    )

    print("\n=== CREATED CAR ===")
    print(test_car.id, test_car.brand, test_car.model)

    # Assign the car to the test user
    assigned = car_manager.assign_car_to_user(
        car_id=test_car.id,
        user_id=test_user.id
    )

    print("\n=== CAR ASSIGNED ===")
    print(f"Car assigned: {assigned}")

    # Update the test car
    updated_car = car_manager.update_car(
        car_id=test_car.id,
        brand="Honda",
        model="Civic"
    )

    print("\n=== UPDATED CAR ===")
    print(updated_car.id, updated_car.brand, updated_car.model)

    # Create a test address
    test_address = address_manager.create_address(
        address="Heredia, Costa Rica",
        user_id=test_user.id
    )

    print("\n=== CREATED ADDRESS ===")
    print(
        test_address.id,
        test_address.address,
        test_address.user_id
    )

    # Update the test address
    updated_address = address_manager.update_address(
        address_id=test_address.id,
        address="Santo Domingo, Heredia"
    )

    print("\n=== UPDATED ADDRESS ===")
    print(
        updated_address.id,
        updated_address.address,
        updated_address.user_id
    )

    # Delete the test address
    deleted_address = address_manager.delete_address(
        address_id=test_address.id
    )

    print("\n=== DELETE ADDRESS ===")
    print(f"Address deleted: {deleted_address}")

    # Delete the test car
    deleted_car = car_manager.delete_car(
        car_id=test_car.id
    )

    print("\n=== DELETE CAR ===")
    print(f"Car deleted: {deleted_car}")

    # Delete the test user
    deleted_user = user_manager.delete_user(
        user_id=test_user.id
    )

    print("\n=== DELETE USER ===")
    print(f"User deleted: {deleted_user}")

    print("\n=== TESTS COMPLETED ===")