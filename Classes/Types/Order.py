from ..User import Customer, Restaurant, Rider
from .OrderStatus import OrderStatus


class Item:
    def __init__(self, id:int, name:str=None, description:str=None, quantity:int=None, cost:float=None):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.cost = cost

    # Getter methods
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_quantity(self):
        return self.quantity
    
    def get_cost(self):
        return self.cost

    # Setter methods
    def set_name(self, name):
        self.name = name
    
    def set_description(self, description):
        self.description = description
    
    def set_quantity(self, quantity):
        self.quantity = quantity
    
    def set_cost(self, cost):
        self.cost = cost
    
    class Builder:
        def __init__(self, id:int):
            self.id = id
            self.name = None
            self.description = None
            self.quantity = None
            self.cost = None

        def with_name(self, name:str):
            self.name = name
            return self
        
        def with_description(self, description:str):
            self.description = description
            return self
        
        def with_quantity(self, quantity:int):
            self.quantity = quantity
            return self
        
        def with_cost(self, cost:float):
            self.cost = cost
            return self

        def build(self):
            return Item(id=self.id, name=self.name, description=self.description, quantity=self.quantity, cost=self.cost)

class Order:
    def __init__(self, id:int, item:Item, placed_at:Restaurant=None,placed_by:Customer=None, status:OrderStatus=None, value:float=None):
        self.id = id
        self.item = item
        self.placed_at = placed_at
        self.placed_by = placed_by
        self.status = status
        self.value = value

    # Getter methods
    def get_id(self):
        return self.id
    
    def get_item(self):
        return self.item
    
    def get_placed_at(self):
        return self.placed_at
    
    def get_placed_by(self):
        return self.placed_by
    
    def get_status(self):
        return self.status
    
    def get_value(self):
        return self.value

    # Setter methods
    def set_placed_at(self, placed_at):
        self.placed_at = placed_at
        
    def set_placed_by(self, placed_by):
        self.placed_by = placed_by
    
    def set_status(self, status):
        self.status = status
    
    def set_value(self, value):
        self.value = value
        
    class Builder:
        def __init__(self, id:int):
            self.id = id
            self.item = None
            self.placed_at = None
            self.placed_by = None
            self.status = None
            self.value = None

        def with_item(self, item:Item):
            self.item = item
            return self
        
        def with_placed_at(self, placed_at:Restaurant):
            self.placed_at = placed_at
            return self
        
        def with_placed_by(self, placed_by:Customer):
            self.placed_by = placed_by
            return self
        
        def with_status(self, status:OrderStatus):
            self.status = status
            return self
        
        def with_value(self, value:float):
            self.value = value
            return self

        def build(self):
            return Order(id=self.id, item=self.item, placed_at=self.placed_at,placed_by=self.placed_by, status=self.status, value=self.value)

class CustomerOrder(Order):
    def __init__(self, id:int, item_name:str=None, item_description:str=None, placed_by:Customer=None, placed_on:Restaurant=None, fulfilled_by:Rider=None):
        super().__init__(id, Item(name=item_name, description=item_description), placed_at=placed_on)
        self.placed_by = placed_by
        self.placed_on = placed_on
        self.fulfilled_by = fulfilled_by

    # Getter methods
    def get_placed_by(self):
        return self.placed_by
    
    def get_fulfilled_by(self):
        return self.fulfilled_by

    # Setter methods
    def set_fulfilled_by(self, fulfilled_by):
        self.fulfilled_by = fulfilled_by

    # Builder pattern implementation
    class Builder:
        def __init__(self, id:int):
            self.id = id
            self.item_name = None
            self.item_description = None
            self.placed_by = None
            self.placed_on = None
            self.fulfilled_by = None

        def with_item(self, name:str, description:str):
            self.item_name = name
            self.item_description = description
            return self
        
        def placed_by(self, placed_by:Customer):
            self.placed_by = placed_by
            return self
        
        def placed_on(self, placed_on:Restaurant):
            self.placed_on = placed_on
            return self
        
        def fulfilled_by(self, fulfilled_by:Rider):
            self.fulfilled_by = fulfilled_by
            return self

        def build(self):
            return CustomerOrder(id=self.id, item_name=self.item_name, item_description=self.item_description, placed_by=self.placed_by, placed_on=self.placed_on, fulfilled_by=self.fulfilled_by)