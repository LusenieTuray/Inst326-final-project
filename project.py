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
    pairs_stocked = 0

    for shoe in inventory:
        room_left = inventory[shoe]["capacity"] - inventory [shoe]["shelf"]
        in_backroom = invenory[shoe]["backroom"]

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
