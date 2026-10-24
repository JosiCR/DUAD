
from decimal import Decimal

from sqlalchemy import select

from database import SessionLocal
from models import Invoice, InvoiceItem, Product


class PurchaseManager:
    def purchase(self, user_id, product_id, quantity):
        if quantity <= 0:
            return {"error": "Quantity must be positive"}, 400

        with SessionLocal() as session:
            try:
                product = session.scalar(
                    select(Product)
                    .where(Product.id == product_id)
                    .with_for_update()
                )

                if product is None:
                    return {"error": "Product not found"}, 404

                if product.quantity < quantity:
                    return {"error": "Insufficient stock"}, 409

                unit_price = Decimal(str(product.price))
                total = unit_price * quantity

                invoice = Invoice(
                    user_id=user_id,
                    total=total,
                )
                session.add(invoice)
                session.flush()

                item = InvoiceItem(
                    invoice_id=invoice.id,
                    product_id=product.id,
                    quantity=quantity,
                    unit_price=unit_price,
                )
                session.add(item)

                product.quantity -= quantity

                session.commit()
                session.refresh(invoice)

                return {
                    "message": "Purchase completed successfully",
                    "invoice": {
                        "id": invoice.id,
                        "user_id": invoice.user_id,
                        "total": str(invoice.total),
                        "created_at": invoice.created_at.isoformat(),
                        "items": [
                            {
                                "product_id": product.id,
                                "product_name": product.name,
                                "quantity": quantity,
                                "unit_price": str(unit_price),
                            }
                        ],
                    },
                }, 201

            except Exception:
                session.rollback()
                raise


purchase_manager = PurchaseManager()
