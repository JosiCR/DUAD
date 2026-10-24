
from database import Base, engine
from models import User, Product, Invoice, InvoiceItem

Base.metadata.create_all(engine)

print("Database tables are ready!")
