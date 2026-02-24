from datetime import datetime, date

def parse_date_str(s: str) -> date:
    """
    Parse date in dd/mm/YYYY, raise ValueError if invalid.
    """
    try:
        dt = datetime.strptime(s, "%d/%m/%Y")
        return dt.date()
    except Exception as e:
        raise ValueError("Invalid date format, expected dd/mm/YYYY") from e

def is_future_date(d: date) -> bool:
    today = date.today()
    return d > today

def format_currency(amount: float) -> str:
    # Not locale-dependent, simple display with 2 decimals
    return f"₡{amount:,.2f}"

def validate_positive_amount(amount):
    if amount <= 0:
        raise ValueError("The amount must be greater than zero.")