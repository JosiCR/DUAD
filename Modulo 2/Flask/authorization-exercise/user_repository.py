
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from database import SessionLocal
from models import User


class UserRepository:
    def create(self, username, password, role="user"):
        try:
            with SessionLocal() as session:
                user = User(
                    username=username,
                    password=generate_password_hash(password),
                    role=role,
                )

                session.add(user)
                session.commit()
                session.refresh(user)

                return {
                    "id": user.id,
                    "username": user.username,
                    "role": user.role,
                }

        except IntegrityError:
            return None

    def get_by_credentials(self, username, password):
        with SessionLocal() as session:
            statement = select(User).where(User.username == username)
            user = session.scalars(statement).first()

            if user is None:
                return None

            if not check_password_hash(user.password, password):
                return None

            return {
                "id": user.id,
                "username": user.username,
                "role": user.role,
            }

    def get_by_id(self, user_id):
        with SessionLocal() as session:
            statement = select(User).where(User.id == user_id)
            user = session.scalars(statement).first()

            if user is None:
                return None

            return {
                "id": user.id,
                "username": user.username,
                "role": user.role,
            }


user_repository = UserRepository()
