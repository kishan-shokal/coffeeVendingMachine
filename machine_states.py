

from abc import ABC, abstractmethod

from coffee import CoffeeFactory
from coffee_decorators import Milk, Sugar 
from errors import OutOfStockError
# from inventory import Inventory
# from machine import CoffeeVendingMachine

class MachineState(ABC):
    @abstractmethod
    def handle(self, machine, action:str):
        pass


class IdleState(MachineState):
    def handle(self, machine, action):
        print("💤 Waiting for selection...")
        machine.set_state(SelectionState())


class SelectionState(MachineState):
    def handle(self, machine, action):
        machine.coffee = CoffeeFactory.create_coffee(action)
        print(f"☕ {action} selected")
        machine.set_state(AddOnsState())


class AddOnsState(MachineState):
    def handle(self, machine, action):
        if action == "done":
            print("➡ Moving to payment...")
            cost = machine.coffee.get_cost()
            machine.set_state(PaymentState())
        elif action == "sugar":
            machine.coffee = Sugar(machine.coffee)
            print(" + Sugar added")
        elif action == "milk":
            machine.coffee = Milk(machine.coffee)
            print(" + Extra milk added")
        else:
            print("❌ Unknown add-on")


class PaymentState(MachineState):
    def handle(self, machine, action):
        if action == "pay":
            print("💰 Payment received")
            machine.set_state(BrewingState())
        else:
            print("❌ Please insert payment.")


class BrewingState(MachineState):
    def handle(self, machine, action):
        print("🔄 Brewing in progress...")
        try:
            machine.coffee.prepare(machine.inventory)
            machine.set_state(DispensingState())
        except OutOfStockError as e:
            print(f"⚠️ Cannot brew : {e}")
            machine.set_state(OutOfServiceState())


class DispensingState(MachineState):
    def handle(self, machine, action):
        # import pdb;pdb.set_trace()
        print("✅ Coffee ready! Enjoy ☕")
        print(f"_______Total cost: ${machine.coffee.get_cost():.2f}")
        machine.set_state(IdleState())


class OutOfServiceState(MachineState):
    def handle(self, machine, action):
        print("🚫 Machine out of service. Call maintenance.")
