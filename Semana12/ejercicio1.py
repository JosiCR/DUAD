
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Balance: ${self.balance}")
    

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

class SavingAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("withdrawal amount must be positive.")
        elif self.balance - amount < self.min_balance:
            print(f"Cannot withdraw. minimum balance of ${self.min_balance} must bw maintained")
        else:
            self.balance -= amount
            print(f"withdrawal successful. Balance: ${self.balance}")



