from .Types.Location import Latlng
# from .Types.Order import Order
from typing import List,Any

class User:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    # Getter methods
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type

    # Setter methods
    def set_name(self, name):
        self.name = name
    
    def set_type(self, type):
        self.type = type

    # Builder pattern implementation
    class Builder:
        def __init__(self, name: str, type: str):
            self.name = name
            self.type = type

        def with_name(self, name: str):
            self.name = name
            return self
        
        def with_type(self, type: str):
            self.type = type
            return self

        def build(self):
            return User(name=self.name, type=self.type)

class Rider(User):
    def __init__(self, name: str, type: str, id: int=None, current_location: Latlng=None, deliveries: List[Any]=[]):
        super().__init__(name, type)
        self.id = id
        self.current_location = current_location
        self.deliveries = deliveries

    # Getter methods
    def get_id(self):
        return self.id
    
    def get_current_location(self):
        return self.current_location
    
    def get_deliveries(self):
        return self.deliveries

    # Setter methods
    def set_id(self, id):
        self.id = id
    
    def set_current_location(self, current_location):
        self.current_location = current_location
    
    def set_deliveries(self, deliveries):
        self.deliveries = deliveries

    # Builder pattern implementation
    class Builder(User.Builder):
        def __init__(self, name: str, type: str):
            super().__init__(name, type)
            self.id = None
            self.current_location = None
            self.deliveries = []

        def with_id(self, id: int):
            self.id = id
            return self
        
        def with_current_location(self, current_location: Latlng):
            self.current_location = current_location
            return self
        
        def with_deliveries(self, deliveries: List[Any]):
            self.deliveries = deliveries
            return self

        def build(self):
            return Rider(name=self.name, type=self.type, id=self.id, current_location=self.current_location, deliveries=self.deliveries)

class Restaurant(User):
    def __init__(self, name: str, type: str, id=None, location: Latlng=None):
        super().__init__(name, type)
        self.id = id
        self.location = location
        self.has_delivery_for = []

    # Getter methods
    def get_id(self):
        return self.id
    
    # def get_orders(self):
    #     return self.orders
    
    # def get_delivery_for(self):
    #     return self.has_delivery_for
    
    def get_location(self):
        return self.location

    # Setter methods
    def set_id(self, id):
        self.id = id
    
    # def set_orders(self, orders):
    #     self.orders = orders
    
    # def set_delivery_for(self,customer):
    #     return self.has_delivery_for.push(customer)
    
    def set_location(self, location):
        self.location = location

    # Builder pattern implementation
    class Builder(User.Builder):
        def __init__(self, name: str, type: str):
            super().__init__(name, type)
            self.id = None
            # self.orders = []
            self.location = None

        def with_id(self, id):
            self.id = id
            return self
        
        # def with_orders(self, orders: List[Order]):
        #     self.orders = orders
        #     return self
        
        def with_location(self, location: Latlng):
            self.location = location
            return self

        def build(self):
            return Restaurant(name=self.name, type=self.type, id=self.id, location=self.location)

class Customer(User):
    def __init__(self, name: str, type: str, id: int=None, location: Latlng=None):
        super().__init__(name, type)
        self.id = id
        # self.orders = orders
        self.location = location

    # Getter methods
    def get_id(self):
        return self.id
    
    # def get_orders(self):
    #     return self.orders
    
    def get_location(self):
        return self.location

    # Setter methods
    def set_id(self, id):
        self.id = id
    
    # def set_orders(self, orders):
    #     self.orders = orders
    
    def set_location(self, current_location):
        self.location = current_location

    # Builder pattern implementation
    class Builder(User.Builder):
        def __init__(self, name: str, type: str):
            super().__init__(name, type)
            self.id = None
            # self.orders = []
            self.location = None

        def with_id(self, id: int):
            self.id = id
            return self
        
        # def with_orders(self, orders: List[Order]):
        #     self.orders = orders
        #     return self
        
        def with_location(self, current_location: Latlng):
            self.location = current_location
            return self

        def build(self):
            return Customer(name=self.name, type=self.type, id=self.id, location=self.location)