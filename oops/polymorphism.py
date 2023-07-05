'''
Polymorphism is one of the pillar of OOP. The word means a method having multiple forms. When a class is inherited 
from superclass, methods are overridden or overloaded.
'''
        
class Account:
    def __init__(self, acc_num: str, balance: float) -> None:
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount:float)->None:
        self.balance += amount
        print(f"Deposited {amount} into account {self.acc_num}. New balance: {self.balance}")

    def withdraw(self, amount:float)->None:
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.acc_num}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in account {self.acc_num}. Withdrawal failed.")


class SavingsAccount(Account):
    def __init__(self, acc_num:str, balance:float, interest_rate:float)->None:
        super().__init__(acc_num, balance)
        self.interest_rate = interest_rate

    def apply_interest(self)->None:
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied to savings account {self.acc_num}. New balance: {self.balance}")

    def withdraw(self, amount:float)->None:
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from savings account {self.acc_num}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in savings account {self.acc_num}. Withdrawal failed.")


class LoanAccount(Account):
    def __init__(self, acc_num:str, balance:float, interest_rate:float)->None:
        super().__init__(acc_num, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount:float, extra_info:float)->None:
        self.balance += amount
        print(f"Deposited {amount} into loan account {self.acc_num}. Extra Info: {extra_info}. New balance: {self.balance}")

    def withdraw(self, amount:float)->None:
        print(f"Cannot withdraw from a loan account. Please contact the bank for repayment.")


# Create instances of different accounts
savings = SavingsAccount("SAV-123", 1000, 0.05)
loan = LoanAccount("LN-456", 2000, 0.1)


# Polymorphism through Method Overloading
savings.deposit(500)  # Output: Deposited 500 into account SAV-123. New balance: 1500
loan.deposit(500, "Additional Info")  # Output: Deposited 500 into loan account LN-456. Extra Info: Additional Info. New balance: 2500

# Polymorphism through Method Overriding
savings.withdraw(200)  # Output: Withdrew 200 from savings account SAV-123. New balance: 1300
loan.withdraw(200)  # Output: Cannot withdraw from a loan account. Please contact the bank for repayment.

# Additional functionality specific to SavingsAccount
savings.apply_interest()  # Output: Interest applied to savings account SAV-123. New balance: 1365.0
