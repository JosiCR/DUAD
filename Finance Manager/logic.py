from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import List, Optional
from utils import parse_date_str, is_future_date


@dataclass
class Category:
    name: str
    color: Optional[str ] = None

    def to_dict(self):
        return asdict(self)
    

@dataclass
class Transaction:
    date: date
    title: str
    amount: float
    category: str
    type: str

    def to_dict(self):
        return {
            "date": self.date.strftime("%d/%m/%Y"),
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "type": self.type
        }
    
class FinanceManager:
    def __init__(self, persistence):
        self.persistence = persistence
        self.categories: List[Category] = []
        self.transactions: List[Transaction] = []
        self.load()

    def load(self):
        data = self. persistence.load_all()
        cats = data.get("categories", [])
        txs = data.get("transactions", [])
        self.categories = [Category(**c) for c in cats]
        self.transactions = []
        for t in txs:
            dt = parse_date_str(t["date"])
            self.transactions.append(Transaction(
                date=dt,
                title=t["title"],
                amount=float(t["amount"]),
                category=t["category"],
                type=t["type"]
            ))

    def save(self):
        cats = [c.to_dict() for c in self.categories]
        txs = [t.to_dict() for t in self.transactions]
        self.persistence.save_all({"categories": cats, "transactions": txs})

    # Category operations
    def add_category(self, name: str, color: Optional[str] = None):
        name = name.strip()
        if not name:
            raise ValueError("Category name cannot be empty")
        if any(c.name.lower() == name.lower() for c in self.categories):
            raise ValueError("Category already exists")
        self.categories.append(Category(name=name, color=color))
        self.save()

    # Transaction operations
    def add_transaction(self, title: str, amount: float, category_name: str, type_: str, date_obj: date):
        title = title.strip()
        if not title:
            raise ValueError("Title cannot be empty")
        if category_name not in [c.name for c in self.categories]:
            raise ValueError("Category does not exist")
        if type_ not in ("Income", "Expense"):
            raise ValueError("Type must be Income or Expense")
        if amount == 0:
            raise ValueError("Amount cannot be zero")
        if is_future_date(date_obj):
            raise ValueError("Date cannot be in the future")
        tx = Transaction(date=date_obj, title=title, amount=float(amount), category=category_name, type=type_)
        self.transactions.append(tx)
        self.save()

    def totals(self):
        incomes = sum(t.amount for t in self.transactions if t.type == "Income")
        expenses = sum(abs(t.amount) for t in self.transactions if t.type == "Expense")
        balance = incomes - expenses
        return {"incomes": incomes, "expenses": expenses, "balance": balance}

    def export_csv(self, path: str):
        import csv
        with open(path, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Fecha", "Título", "Monto", "Categoría", "Tipo"])
            for t in self.transactions:
                writer.writerow([t.date.strftime("%d/%m/%Y"), t.title, t.amount, t.category, t.type])
            writer.writerow([])
            totals = self.totals()
            writer.writerow([])
            writer.writerow(["Totals:", "", ""])
            writer.writerow(["Incomes", totals["incomes"]])
            writer.writerow(["Expenses", totals["expenses"]])
            writer.writerow(["Balance", totals["balance"]])
        

