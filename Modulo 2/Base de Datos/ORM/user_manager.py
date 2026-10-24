from sqlalchemy import select

from models import User


class UserManager:
    def __init__(self, session):
        self.session = session

    def create_user(self, name, email):
        user = User(
            name=name,
            email=email
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    def update_user(self, user_id, name=None, email=None):
        statement = select(User).where(User.id == user_id)
        user = self.session.scalars(statement).first()

        if user is None:
            return None

        if name is not None:
            user.name = name

        if email is not None:
            user.email = email

        self.session.commit()
        self.session.refresh(user)

        return user

    def delete_user(self, user_id):
        statement = select(User).where(User.id == user_id)
        user = self.session.scalars(statement).first()

        if user is None:
            return False

        self.session.delete(user)
        self.session.commit()

        return True

    def get_all_users(self):
        statement = select(User)
        return self.session.scalars(statement).all()