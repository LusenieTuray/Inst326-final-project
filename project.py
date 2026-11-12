import random
class Shoe:
    
    def __init__(self, name, type = ""):
        self.type = type
        self.name = name
        if type == "Formal":
            self.price = 80
        elif type == "Casual":
            self.price = 70
        elif type == "Sport":
            self.price = 90
        elif type == "Boots":
            self.price = 60
        else:
            self.price = 50
            
class Customer():
    
    def __init__(self, name, type): 
        self.name = name
        self.type = type
        self.budget = random.randint(50, 100)
    def __repr__(self):
        return f"{self.name} like's {self.type}"
        
        
def generate_customers():
    todays_cust = []
    num_customers = random.randint(3, 10)
    
    for i in range(num_customers):
        cust_type = "" 
        random_type = random.randint(1, 4)
        
        if random_type == 1:
            cust_type = "Formal"
        elif random_type == 2:
            cust_type = "Casual"
        elif random_type == 3:
            cust_type = "Sport"
        else:
            cust_type = "Boots"
            
        variable_name = f"customer_{i}"
        todays_cust.append(Customer(f"Customer {i}", cust_type))
        
    return todays_cust

list = generate_customers()
print(list)


def maintain_store(inventory, cleaning_mins, cleanliness):
    """ Restock the shelves, clean the store, and figure out customer satisfaction.
 
    Args:
        inventory (dict): Each shoe type maps to a dict with "backroom",
            "shelf", and "capacity" (all ints).
            Example: {"boots": {"backroom": 10, "shelf": 2, "capacity": 8}}
        cleaning_mins (int): Minutes spent cleaning the store.
        cleanliness (int): Cleanliness score before cleaning (0 to 100).
 
    Returns:
        dict: The new "cleanliness" score, the "satisfaction" score,
            and the number of "pairs_stocked".
 
    Side effects:
        Moves shoes from the backroom to the shelf in the inventory.
        """
    pairs_stocked = 0

    for shoe in inventory:
        room_left = inventory[shoe]["capacity"] - inventory [shoe]["shelf"]
        in_backroom = inventory[shoe]["backroom"]

    if in_backroom < room_left:
        amount = in_backroom
    else:
        amount = room_left
    inventory[shoe]["shelf"] = inventory[shoe]["shelf"] + amount
    inventory[shoe]["backroom"] = inventory[shoe]["backroom"] - amount
    pairs_stocked = pairs_stocked + amount

    cleanliness = cleanliness + cleaning_mins * 2
    if cleanliness > 100:
        cleanliness = 100

    full_shelves = 0
    for shoe in inventory:
        if inventory[shoe]["shelf"] == inventory[shoe]["capacity"]:
            full_shelves = full_shelves + 1
    satisfaction = cleanliness // 2 + full_shelves * 10
    if satisfaction > 100:
        satisfaction = 100
    return {
        "cleanliness": cleanliness,
        "satisfaction": satisfaction,
        "pairs_stocked": pairs_stocked,
    }

fake_inventory = {
    "sports": {"backroom": 12, "shelf": 3, "capacity": 10},
    "boots": {"backroom": 2, "shelf": 1, "capacity": 8},
    "formal": {"backroom": 0, "shelf":6, "capacity": 6},
    "casual": {"backroom": 20, "shelf": 0, "capacity": 12},
}

result = maintain_store(fake_inventory, 15, 55)
print(result)
print(fake_inventory)

def big_decisions(store, hire, ad, hire_cost, ad_cost, emp_needed):
    
    for emp in range(hire):
        if store["money"] < hire_cost:
            print(f"You hired {emp+1} employee(s). You need more money to hire "
                  "another employee.")
            break
        else:
            store["money"] -= hire_cost
            store["num_employees"] += 1
    
    if ad:
        if store["money"] < ad_cost:
            print(f"You need an additional ${ad_cost - store["money"]} to post "
                  f"an advertisement.")
        else:
            store["money"] -= ad_cost
            store["num_customers"] += random.randint(2, 10)
            print("Your advertisement post attracted more customers.")
    
    if store["num_employees"] < emp_needed:
        print("Your store could still use more employees.")
        
    print(f"Money remaining: ${store["money"]}\nEmployees: "
          f"{store["num_employees"]}\nCustomers: {store["num_customers"]}")
    
    
fake_store = {
    "money" : 2500,
    "num_employees" : 5,
    "num_customers" : 15
}

big_decisions(fake_store, 6, True, 400, 300, 5)