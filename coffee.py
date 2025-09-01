from abc import ABC, abstractmethod

# from inventory import Inventory
from errors import CoffeeNotFoundError


class CoffeeInterface(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def prepare(self, inventory) -> str:
        pass 

    @abstractmethod
    def get_cost(self) -> float:
        pass

    def requirements(self) -> dict:
        return {}
    



class SimpleCoffee(CoffeeInterface):
    def requirements(self) -> dict:
        return {"water": 100, "coffee_beans": 10}

    def get_cost(self) -> float:
        return 5.0

    def prepare(self, inventory) -> str:
        inventory.consume_item(self.requirements())
        print("☕ Preparing Simple Coffee")
        return "Simple Coffee ready!"


class Cappuccino(CoffeeInterface):
    def requirements(self) -> dict:
        return {"water": 80, "coffee_beans": 12, "milk": 50, "sugar": 5}

    def get_cost(self) -> float:
        return 8.0

    def prepare(self, inventory) -> str:
        inventory.consume_item(self.requirements())
        print("☕ Preparing Cappuccino")
        return "Cappuccino ready!"


class Latte(CoffeeInterface):
    def requirements(self) -> dict:
        return {"water": 70, "coffee_beans": 10, "milk": 100, "sugar": 5}

    def get_cost(self) -> float:
        return 9.0

    def prepare(self, inventory) -> str:
        inventory.consume_item(self.requirements())
        print("☕ Preparing Latte")
        return "Latte ready!"


class CoffeeFactory:
    @staticmethod
    def create_coffee(coffee_type: str) -> CoffeeInterface:
        coffee_type = coffee_type.lower()
        if coffee_type == "simple":
            return SimpleCoffee()
        elif coffee_type == "cappuccino":
            return Cappuccino()
        elif coffee_type == "latte":
            return Latte()
        else:
            raise CoffeeNotFoundError(coffee_type)
