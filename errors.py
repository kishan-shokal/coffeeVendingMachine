

class OutOfStockError(Exception):
    def __init__(self, item):
        self.item = item
        super().__init__(f"Item '{item}' is out of stock.")

class ItemNotFoundError(Exception): 
    def __init__(self, name):
        super().__init__(f"Item '{name}' not found in inventory.")

class CoffeeNotFoundError(Exception):
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type
        super().__init__(f"Coffee type '{coffee_type}' not found.")