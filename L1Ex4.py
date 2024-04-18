class Account:
    def __init__(self, balance: int, name: str):
        self.name = name
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self.balance += amount

    def take(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough balance")
        self.balance -= amount
