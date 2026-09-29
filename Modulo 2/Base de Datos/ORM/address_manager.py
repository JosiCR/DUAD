from sqlalchemy import select

from models import Address


class AddressManager:
    def __init__(self, session):
        self.session = session

    def create_address(self, address, user_id):
        new_address = Address(
            address=address,
            user_id=user_id
        )

        self.session.add(new_address)
        self.session.commit()
        self.session.refresh(new_address)

        return new_address

    def update_address(self, address_id, address=None, user_id=None):
        statement = select(Address).where(Address.id == address_id)
        address_object = self.session.scalars(statement).first()

        if address_object is None:
            return None

        if address is not None:
            address_object.address = address

        if user_id is not None:
            address_object.user_id = user_id

        self.session.commit()
        self.session.refresh(address_object)

        return address_object

    def delete_address(self, address_id):
        statement = select(Address).where(Address.id == address_id)
        address_object = self.session.scalars(statement).first()

        if address_object is None:
            return False

        self.session.delete(address_object)
        self.session.commit()

        return True

    def get_all_addresses(self):
        statement = select(Address)
        return self.session.scalars(statement).all()