from abc import ABC, abstractmethod 
from enum import Enum

class Bank(Enum):
    SBI = "State Bank of India"
    AXI = "Axis Bank"
    ICI = "ICICI Bank"

class Account:
    acc_set = set()
    def __init__(self, acc_num:str , initial_balance:float=0)->None:
        if acc_num not in Account.acc_set: 
            self.__acc_num = acc_num  
            self.__balance = initial_balance 
            Account.acc_set.add(acc_num)
        else:
            print('Account exist.')
            raise ValueError (f'Account exist.')
        
    @property
    def status(self)->float:
        return self.__balance
        
    def deposit(self, amount:float)->bool:
        if amount <=0:
            return False 
        self.__balance += amount 
        return True 
    
    def withdraw(self, amount:float)->bool:
        if amount> self.__balance:
            return False
        self.__balance -= amount 
        return True
    
class ATM(ABC):
    
    @abstractmethod 
    def get_bank_info(self, card_num: str)->bool:
        pass 
    
    @abstractmethod
    def deposit_money(self, card_num: str, amount: float)->None:
        pass 
    
    @abstractmethod
    def withdraw_money(self, card_num: str, amount: float)->None:
        pass 
    
class SBI_ATM(ATM):
    
    def get_bank_info( self, card_num:str)->bool:
        try:
            bank_code = card_num[:3]
            return Bank[bank_code].value
        except KeyError as error:
            return False
        
    def deposit_money( self, card_number:str, amount:float)->None:
        transaction_account = alloted_cards[card_number]
        if transaction_account.deposit(amount):
            print(transaction_account.status)
        else:
            print('deposit failed.')
                
            
    def withdraw_money( self, card_number:str, amount:float)->None:
        transaction_account = alloted_cards[card_number] 
        if transaction_account.withdraw(amount):
            print(transaction_account.status)
        else:
            print('Withdrawal failed.')
        
        
bank_acc_num_list=[
    'SBI1234',
    'AXI1234',
    'BOI1234',
    'ICI1234'
]

alloted_cards = {} 
for acc in bank_acc_num_list:
    try:
        account=Account(acc, 1000)
        alloted_cards[acc] = account
    except:
        print(f'Account creatiion failed for {acc}')

sbi_atm=SBI_ATM()

for card_num, account in alloted_cards.items():
    if sbi_atm.get_bank_info(card_num):
        sbi_atm.deposit_money(card_num,500)
        sbi_atm.withdraw_money(card_num, 850)
        

    
            
        
    