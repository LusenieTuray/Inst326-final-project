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
