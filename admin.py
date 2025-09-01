
from machine_states import IdleState
class Admin:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        info = f"Admin Username: {self.username}, Email: {self.email}"
        return info 

    def update(self, message):
        print(f"[Notification for {self.username}] {message}")

    def refill(self,inventry,items):
        for item, quantity in items.items():
            inventry.add_item(item, quantity)
        for machine in inventry.machines:
            if machine.state.__class__.__name__ == "OutOfServiceState":
                machine.set_state(IdleState()) 

    
        




