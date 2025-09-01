from inventory import Inventory 
from machine import CoffeeVendingMachine
from admin import Admin

if __name__ == "__main__":
    admin = Admin("Kishan","kishan@gmail.com")


    

    inventory = Inventory()
    machine = CoffeeVendingMachine(inventory)
    inventory.add_observer(admin)
    inventory.add_machine(machine)

    
    inventory.add_item("water", 100, alert_limit=200, capacity=2000)        
    inventory.add_item("coffee_beans", 500, alert_limit=100, capacity=1000)  
    inventory.add_item("milk", 80, alert_limit=150, capacity=1500)          
    inventory.add_item("sugar", 30, alert_limit=50, capacity=500)          
    print("📦 Initial Inventory:")
    inventory.display_inventory()
    print("-" * 40) 


    try:



        for _ in range(5):
            
            machine.request()                     
            machine.request("latte")  
            machine.request("milk")                
            machine.request("sugar")              
            machine.request("done")               
            machine.request("pay")                 
            machine.request()   
            machine.request()


            

            print("📦 Inventory After Transaction:")
            inventory.display_inventory()
            print("-" * 40) 

            if _ == 3:
                items={
                    "milk":500,
                    "sugar": 200,
                    "water": 1000,
                    "coffee_beans": 300
                }
                admin.refill(inventory,items)

            print("📦 Inventory After Restock:")    
    except Exception as e:
        print(f"Error: {e}")


