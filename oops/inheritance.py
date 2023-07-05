'''
It allows us to create new classes (derived or child classes) based on existing classes (base or parent classes).
It enables code reuse and promotes the principle of "is-a" relationship between classes.

By default, each class inherit base object class.
'''

class Account:
    def __init__(self, account_number:str, balance:float)->None:
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount:float)->None:
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount:float)->None:
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def display_balance(self)->None:
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number:str, balance:float, interest_rate:float)->None:
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self)->None:
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Calculated interest: {interest}. Current balance: {self.balance}")


class CurrentAccount(Account):
    def __init__(self, account_number:str, balance:float, overdraft_limit:float)->None:
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount:float)->None:
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient balance and overdraft limit.")


# Create a savings account and perform operations
savings = SavingsAccount("SAV123", 5000, 0.05)
savings.display_balance()
savings.deposit(2000)
savings.calculate_interest()
savings.withdraw(3000)

# Create a current account and perform operations
current = CurrentAccount("CUR456", 10000, 5000)
current.display_balance()
current.deposit(500)
current.withdraw(15000)
