'''
Encapsulation is one of the pillar of OOP principle. It refers to bundling of data and methods within a class.
It is done so that attributes, methods are only accessible by class only(hidden from outside-> access modifiers).
This helps in achieving data integrity and code orgnization.

concept-name mangaling
'''

class bankaccount:
    
    __bank_account_num_set = set()
    
    def __init__(self, acc_num: str , initial_balance : float = 0.0) -> None :
        if acc_num not in bankaccount.__bank_account_num_set:
            self.__acc_num =acc_num 
            self.__balance = initial_balance
            bankaccount.__bank_account_num_set.add(acc_num)
        else:
            raise ValueError(f' Bank Account already present in the system')
        
    @property
    def acc_num(self) ->str:
        return self.__acc_num 
    
    @property
    def balance(self) ->float:
        return self.__balance 
    
    @balance.setter
    def balance(self, amount : float)-> None:
        if amount>=0.0:
            self.__balance = amount
        else:
            raise ValueError(f' Can not set the amount to be negative')
        
    def withdraw(self, amount: float) ->str:
        if amount > self.__balance:
            return f' Amount requested is more than balance. Withdrrawal failed'
        else:
            self.__balance -= amount 
            return f' Thanks for using the service. Banlance has been updated. Withdrawal amount is Rs {amount}/- '
        
bank_acc_num_list=[
    'abc1234',
    'abc1234',
    'qwe1234',
    'asd1234'
]
print('creating accounts')
account_set = set()
for acc in bank_acc_num_list:
    try:
        account = bankaccount(acc,100.0)
        account_set.add(account)
        print(f' Account created with acc number {account.acc_num}')
    except ValueError as ve:
        print(f'{ve}')
        
print('checking balances')
for acc in account_set:
    print(f' We have {acc.balance} in {acc.acc_num}')

print('Updating balances')
for acc in account_set:
    try:
        acc.balance = 1000.58
        print(f' We have {acc.balance} in {acc.acc_num}')
    except ValueError as ve:
        print(f'{ve}') 
        
print('checking balances')
for acc in account_set:
    print(f' We have {acc.balance} in {acc.acc_num}')
    
print('Withdrawing amount')
for acc in account_set:
    print(acc.withdraw(700))
    
print('checking balances')
for acc in account_set:
    print(f' We have {acc.balance} in {acc.acc_num}')
        
    
        
    
    
        
    
        