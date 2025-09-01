

from coffee import CoffeeInterface 

# from inventory import Inventory


class CoffeeDecorator(CoffeeInterface):

    def __init__(self, coffee: CoffeeInterface):
        self._coffee = coffee  


class Sugar(CoffeeDecorator):
    def prepare(self, inventory):
        self._coffee.prepare(inventory)
        inventory.consume_item(self.requirements())
        print(" + Adding Sugar")

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.2

    def requirements(self) -> dict:
        return {"sugar": 1}


class Milk(CoffeeDecorator):
    def prepare(self, inventory):
        self._coffee.prepare(inventory)
        inventory.consume_item(self.requirements())
        print(" + Adding Extra Milk")

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.5

    def requirements(self) -> dict:
        return {"milk": 1}


