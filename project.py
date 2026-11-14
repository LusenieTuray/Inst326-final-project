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
    """
    Creates a random number of customers for the day.

    Args:
        None

    Returns:
        list: A list of Customer objects for the day.

    Side Effects:
        Creates Customer objects.
    """

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

def buy_stock(store, inventory):
    """Let the player buy shoes for the backroom until they enter 'done'.

    Each purchase reduces the money available for the next one.

    Args:
        store (dict): Store information containing the current money balance.
        inventory (dict): Shoe types mapped to their stock counts.

    Returns:
        None.

    Side effects:
        Deducts the cost of each purchase from the store's money and adds
        the purchased shoes to the backroom.
    """
    costs = {"formal": 45, "casual": 40, "sports": 55, "boots": 35}

    while True:
        print(f"Money left: ${store['money']}")
        shoe_type = input("Buy formal, casual, sports, boots, or done: ")

        if shoe_type == "done":
            break

        quantity = int(input("How many pairs? "))
        total_cost = costs[shoe_type] * quantity

        if store["money"] >= total_cost:
            store["money"] -= total_cost
            inventory[shoe_type]["backroom"] += quantity
        else:
            print("You don't have enough money for that purchase.")
    
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



def big_decisions(store, hire, hire_cost, ad_cost, emp_needed):
    """
    Decide whether to hire employee(s) and/or pay for an advertising post to
    attract more customers.
    
    Args:
        store (dict) - stores the amounbt of money a store has, the number of
        employees, and number of customers
        hire (int) - provides the number of employees the plaayer wants to hire,
        which could be zero
        hire_cost (int) - the cost of hiring an employee
        ad_cost (int) - the ost of posting an advertisement
        emp_needed (int) - the number of employees needed to keep the 
        store running.

    Returns:
        None
    Side Effects:
        Reduces the store’s available money when an action is taken. 
        May increase the employee count and expected customer numbers.
    """

    for emp in range(hire):
        if store["money"] < hire_cost:
            print(f"You hired {emp+1} employee(s). You need more money to hire "
                  "another employee.")
            break
        else:
            store["money"] -= hire_cost
            store["num_employees"] += 1
    
    print(f"Money remaining: ${store["money"]}\nEmployees: "
          f"{store["num_employees"]}\nCustomers: {store["num_customers"]}")
    
    ad_choice = input(f"You can post an ad for ${ad_cost}. Would you like to?"
                      "(yes/no)")
    if ad_choice == "yes":
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
buy_stock(fake_store, fake_inventory)
result = maintain_store(fake_inventory, 15, 55)
print(result)
print(fake_inventory)

big_decisions(fake_store, 6, 400, 300, 5)
big_decisions(fake_store, 6, 400, 100, 5)




# Function by Lusenie Turay
def calculate_market_demand(store_prices, competitor_prices, base_demand, reputation):

    """
    Calculates shoe demand based on competitor prices and store reputation.

    Args:
        store_prices (dict): Our store's shoe prices.
        competitor_prices (dict): Other stores' shoe prices.
        base_demand (dict): Starting demand for each shoe type.
        reputation (int): Store reputation from 0 to 100.

    Returns:
        dict: The updated demand for each shoe type.

    Raises:
        ValueError: If the inputs are invalid.

    Side Effects:
        None.
    """

    if (not isinstance(reputation, int)
            or isinstance(reputation, bool)
            or not 0 <= reputation <= 100):
        raise ValueError("The Store's reputation must be between 0 and 100.")

    if (store_prices.keys() != competitor_prices.keys()
            or store_prices.keys() != base_demand.keys()):
        raise ValueError("All dictionaries must have the same shoe types.")

    updated_demand = {}

    for shoe_type in store_prices:
        our_price = store_prices[shoe_type]
        competitor_price = competitor_prices[shoe_type]
        demand = base_demand[shoe_type]

        if (not isinstance(our_price, (int, float))
                or isinstance(our_price, bool)
                or not 0 < our_price < float("inf")):
            raise ValueError("Your shoe prices must be positive numbers.")

        if (not isinstance(competitor_price, (int, float))
                or isinstance(competitor_price, bool)
                or not 0 < competitor_price < float("inf")):
            raise ValueError("Competitorshoe prices must be positive numbers.")

        if (not isinstance(demand, int)
                or isinstance(demand, bool) or demand < 0):
            raise ValueError("Base demand must be a nonnegative integer.")

        # Compare our prices with  other company etitor prices
        price_ratio = our_price / competitor_price

        if price_ratio > 1.10:
            demand = demand * 0.80
        elif price_ratio < 0.90:
            demand = demand * 1.15

        # Adjust demand number based on store reputation
        if reputation >= 75:
            demand = demand * 1.10
        elif reputation < 40:
            demand = demand * 0.90

        # Round demand number to a whole number
        updated_demand[shoe_type] = max(0, int(demand + 0.5))

    return updated_demand
