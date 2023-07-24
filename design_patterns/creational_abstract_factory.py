''' 
Abstract factory design pattern is a creational type pattern. It is used to create objects when we have \\
hierarchical classes. Example: A Furtinutue store can have Furniture as main class. It can have sub-categories\\
like old age design, new age design etc, and in each sub categories we can have options like chairs, sofas etc
'''
from abc import ABC, abstractmethod 

# Having an abstract class of furniture to declare a contract of methods to have 
class Furniture(ABC):
    @abstractmethod 
    def describe(self):
        pass 
    
# describing various furnitures
class Gaming_chairs(Furniture):
    def describe(self):
        print('this is a gaming chair')
        
class Gaming_tables(Furniture):
    def describe(self):
        print('this is a gaming table')
        
class Office_chairs(Furniture):
    def describe(self):
        print('this is a office chair')
        
class Office_tables(Furniture):
    def describe(self):
        print('this is a office table')
        
# having an abstract class for a factory 
class Factory(ABC):
    @abstractmethod
    def create_chair(self):
        pass 
    
    @abstractmethod
    def create_table(self):
        pass 
    
# creating factories 
class Gaming_factory(Factory):
    def create_chair(self):
        return Gaming_chairs()
    
    def create_table(self):
        return Gaming_tables() 
    
class Office_factory(Factory):
    def create_chair(self):
        return Office_chairs()
    
    def create_table(self):
        return Office_tables() 
    
def get_furniture(_factory):
    _chair = _factory.create_chair()
    _table = _factory.create_table()
    
    _chair.describe()
    _table.describe()
    
def driver():
    game_factory = Gaming_factory()
    office_factory = Office_factory()
    
    # get gaming set 
    get_furniture(game_factory)
    # get office set 
    get_furniture(office_factory)
    
if __name__=="__main__":
    driver()
    
    
    
        

        
    