
import threading
from typing import Any

class Singleton:
    __instance = None
    __lock = threading.Lock()
    
    def __setattr__(self, attribute: str, attr_value: Any) -> None:
        print(attribute)
        allowed_attributes = ['_Singleton__name']
        if attribute in allowed_attributes:
            if not hasattr(self, attribute):
                super().__setattr__(attribute, attr_value)
            else: 
                raise AttributeError (' Attribute over Riding Not Allowed')
        else:
            raise AttributeError("Adding new attribute not allowed")

    def __new__(cls, name):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(Singleton, cls).__new__(cls)
                    cls.__instance.__name = name
        return cls.__instance


try:
    s1 = Singleton('pg')
    s2 = Singleton('pgthegrt')
except Exception as e:
    print(e)

try:
    s1.__name = 'pgthegrt'
except Exception as e:
    print(e)
    
try:
    s1._Singleton__name = 'pgthegrt'
except Exception as e:
    print(e)   

try:
    s2.age = 25
except Exception as e:
    print(e)  

try:
    print(s1.age)
except Exception as e:
    print(e) 

