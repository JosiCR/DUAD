
from getpass import getpass

from user_repository import user_repository


username = input("Admin username: ").strip()
password = getpass("Admin password: ")

if not username or not password:
    print("Username and password are required.")
else:
    admin = user_repository.create(
        username=username,
        password=password,
        role="admin",
    )

    if admin is None:
        print("Could not create admin. The username may already exist.")
    else:
        print(f"Admin created successfully: {admin['username']}")
