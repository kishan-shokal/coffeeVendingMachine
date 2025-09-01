
import threading

from errors import OutOfStockError, ItemNotFoundError

from admin import Admin 
from singleton_meta import SingletonMeta


class InventoryObserverManager:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class _Item:
    def __init__(self, name, alert_limit=0, capacity=100):
        self._name = name
        self._quantity = 0
        self._alert_limit = alert_limit
        self._capacity = capacity
        self._lock = threading.Lock()

    @property
    def name(self):
        return self._name

    @property
    def alert_required(self):
        return self._quantity <= self._alert_limit

        
    def _add(self, quantity):
        with self._lock:  
            self._quantity = min(self._capacity, self._quantity + quantity)

    def _consume(self, quantity):
        with self._lock:  
            if self._quantity < quantity:
                raise OutOfStockError(self._name)
            self._quantity -= quantity
    def check_quantity(self, quantity):
        return self._quantity >= quantity


    def display(self):
        return f"Item: {self._name}, Quantity: {self._quantity}, Alert Limit: {self._alert_limit}, Capacity: {self._capacity}"



class Inventory(metaclass=SingletonMeta):

    def __init__(self):
        self._items = {}
        self._observer_manager = InventoryObserverManager()
        self.machines = []
        self._lock = threading.Lock()

    def add_machine(self, machine):
        self.machines.append(machine)
        return self 

    def add_item(self, name, quantity, alert_limit=0, capacity=100):
        with self._lock:
            if name not in self._items:
                self._items[name] = _Item(name, alert_limit, capacity)

            item = self._items[name]
            item._add(quantity)

            if item.alert_required:
                self._observer_manager.notify(f"Alert: {item.name} stock is low: {item._quantity}")

    def consume_item(self, items: dict):
        with self._lock:
            for name, quantity in items.items():
                if name not in self._items:
                    raise ItemNotFoundError(name)
                item = self._items[name]
                if not item.check_quantity(quantity):
                    raise OutOfStockError(name)
            for name, quantity in items.items():
                item = self._items[name]
                item._consume(quantity)
                if item.alert_required:
                    self._observer_manager.notify(f"Alert: {name} stock is low: {item._quantity}")


    def display_inventory(self):
        for item in self._items.values():
            print(item.display())

    def add_observer(self, observer):

        self._observer_manager.add_observer(observer)
