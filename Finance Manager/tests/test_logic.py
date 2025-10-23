import os
import tempfile
import pytest
from persistence import Persistence
from logic import FinanceManager
from datetime import date, timedelta

@pytest.fixture
def persistence_tmp(tmp_path):
    p = Persistence(data_dir=str(tmp_path/"data"))
    return p

def test_add_category(persistence_tmp):
    mgr = FinanceManager(persistence_tmp)
    mgr.add_category("Food", "#FFA500")
    assert any(c.name == "Food" for c in mgr.categories)

def test_add_duplicate_category_raises(persistence_tmp):
    mgr = FinanceManager(persistence_tmp)
    mgr.add_category("Bills")
    with pytest.raises(ValueError):
        mgr.add_category("Bills")  # duplicate

def test_add_transaction_without_category_raises(persistence_tmp):
    mgr = FinanceManager(persistence_tmp)
    future_date = date.today()
    with pytest.raises(ValueError):
        mgr.add_transaction("Test", 10, "NonExistent", "Expense", future_date)

def test_add_transaction_future_date_raises(persistence_tmp):
    mgr = FinanceManager(persistence_tmp)
    mgr.add_category("Misc")
    future = date.today() + timedelta(days=5)
    with pytest.raises(ValueError):
        mgr.add_transaction("FutureTx", 10, "Misc", "Income", future)

def test_add_transaction_success(persistence_tmp):
    mgr = FinanceManager(persistence_tmp)
    mgr.add_category("Salary")
    today = date.today()
    mgr.add_transaction("Salary July", 1000.0, "Salary", "Income", today)
    assert any(t.title == "Salary July" for t in mgr.transactions)

def test_totals_calculation(persistence_tmp):
    mgr = FinanceManager(persistence_tmp)
    mgr.add_category("Work")
    mgr.add_category("Food")
    today = date.today()
    mgr.add_transaction("Salary", 2000.0, "Work", "Income", today)
    mgr.add_transaction("Lunch", 20.0, "Food", "Expense", today)
    totals = mgr.totals()
    assert totals["incomes"] == 2000.0
    assert totals["expenses"] == 20.0
    assert totals["balance"] == 1980.0

def test_export_csv_creates_file(persistence_tmp, tmp_path):
    mgr = FinanceManager(persistence_tmp)
    mgr.add_category("X")
    today = date.today()
    mgr.add_transaction("T1", 5.0, "X", "Income", today)
    fp = tmp_path / "out.csv"
    mgr.export_csv(str(fp))
    assert fp.exists()
    content = fp.read_text()
    assert "T1" in content

def test_persistence_loads_saved_data(persistence_tmp):
    mgr = FinanceManager(persistence_tmp)
    mgr.add_category("A")
    today = date.today()
    mgr.add_transaction("Tx", 10, "A", "Expense", today)
    # create new manager with same persistence, should load previous
    mgr2 = FinanceManager(persistence_tmp)
    assert any(c.name == "A" for c in mgr2.categories)
    assert any(t.title == "Tx" for t in mgr2.transactions)