''' 
factory design pattern is a creational type design patterns. It is used when in run time we want to create \\
    different objects(eg: on run time i want to create a connection or MSSQL, sqlite, postgre etc) \\
        or I want objects (eg: for notification service, I want sms as an object, or emailservice as an object etc) \\
            We have a common things among these objects. That it, they will have same methods but implementations will be different.
            Lets try factory method for creating notifications system
            it is factory because, we create objects without specifying the exact class of the object
            or more like we give order in a factory and factory gives us a product
            it helps when the client code needs to be decoupled from the object creation process.
'''
from abc import ABC, abstractmethod 
from enum import Enum 
class NOTIFICATION(ABC):
    @abstractmethod 
    def send(self, msg):
        pass 
    
class SMS(NOTIFICATION):
    def send(self, msg):
        print(f'sending sms.. msg is: {msg} ')
        
class EMAIL(NOTIFICATION):
    def send(self, msg):
        print(f'sending mail...mail msg is: {msg}')
        
class PUSH(NOTIFICATION):
    def send(self, msg):
        print(f'sending push notice...notice is: {msg}')
        
   

class NOTIFICATION_SERVICES(Enum):
    _SMS = SMS()
    _EMAIL = EMAIL()
    _PUSH = PUSH()
    
     
def driver():
    choice = input('What medium of communication service you want?(sms/email/push): ')
    msg = input('Enter your message: ')
    Operator='_'+choice.upper()
    try:
        if NOTIFICATION_SERVICES[Operator]:
            requested_obj = NOTIFICATION_SERVICES[Operator].value 
            requested_obj.send(msg)
    except KeyError:
        print('Choice provided is not supported')
    except Exception as exception:
        print(f'Exception occured while sending. Error is : {exception}')
    finally:
        print('Process Completed')
            
if __name__=='__main__':
    driver()