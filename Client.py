class Client:
    def __init__(self, client_id: int, name: str, balance: float):
        self.client_id = client_id
        self.name = name
        self.balance = balance
        self.current_bike = None
    def has_enough_money(self, amount: float) -> bool:
        return self_balance >=amount
    def deduct_balance(self, amount: float) -> bool:
        if self.has_enough_money(amount):
           self.balance -= amount
           return True
        return False
    def add(self, amount: float):
        if amount > 0:
            self.balance += amount
            return True
        return False
