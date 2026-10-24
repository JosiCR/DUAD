
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    role: Mapped[str] = mapped_column(
        String(20), default="user", nullable=False
    )

    invoices: Mapped[list["Invoice"]] = relationship(
        back_populates="user"
    )


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False
    )
    entry_date: Mapped[date] = mapped_column(
        Date, nullable=False
    )
    quantity: Mapped[int] = mapped_column(
        Integer, nullable=False
    )


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    total: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="invoices"
    )
    items: Mapped[list["InvoiceItem"]] = relationship(
        back_populates="invoice"
    )


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    invoice_id: Mapped[int] = mapped_column(
        ForeignKey("invoices.id"), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"), nullable=False
    )
    quantity: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False
    )

    invoice: Mapped["Invoice"] = relationship(
        back_populates="items"
    )
