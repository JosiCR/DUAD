
from datetime import date
from decimal import Decimal

from sqlalchemy import select

from database import SessionLocal
from models import Product


class ProductManager:
    def create(self, name, price, entry_date, quantity):
        product = Product(
            name=name,
            price=Decimal(str(price)),
            entry_date=date.fromisoformat(entry_date),
            quantity=quantity,
        )

        with SessionLocal() as session:
            session.add(product)
            session.commit()
            session.refresh(product)

            return self._serialize(product)

    def get_all(self):
        with SessionLocal() as session:
            products = session.scalars(select(Product)).all()
            return [self._serialize(product) for product in products]

    def get_by_id(self, product_id):
        with SessionLocal() as session:
            product = session.get(Product, product_id)

            if product is None:
                return None

            return self._serialize(product)

    def update(self, product_id, data):
        with SessionLocal() as session:
            product = session.get(Product, product_id)

            if product is None:
                return None

            if "name" in data:
                product.name = data["name"]

            if "price" in data:
                product.price = Decimal(str(data["price"]))

            if "entry_date" in data:
                product.entry_date = date.fromisoformat(
                    data["entry_date"]
                )

            if "quantity" in data:
                product.quantity = data["quantity"]

            session.commit()
            session.refresh(product)

            return self._serialize(product)

    def delete(self, product_id):
        with SessionLocal() as session:
            product = session.get(Product, product_id)

            if product is None:
                return False

            session.delete(product)
            session.commit()

            return True

    @staticmethod
    def _serialize(product):
        return {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "entry_date": product.entry_date.isoformat(),
            "quantity": product.quantity,
        }


product_manager = ProductManager()
