
from machine_states import  IdleState

class CoffeeVendingMachine:
    def __init__(self, inventory):
        self.state = IdleState()
        self.inventory = inventory
        self.coffee = None  

    def set_state(self, state):
        self.state = state

    def request(self, action=None):
       
        self.state.handle(self, action)

    
