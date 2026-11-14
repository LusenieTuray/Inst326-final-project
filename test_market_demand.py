
import ast


with open("project.py", "r") as file:
    code = file.read()

tree = ast.parse(code)

for item in tree.body:
    if isinstance(item, ast.FunctionDef):
        if item.name == "calculate_market_demand":
            function_code = ast.Module(body=[item], type_ignores=[])
            exec(compile(function_code, "projects.py", "exec"))
            break
else:
    raise ValueError("Market demand function was not found.")



# Test 
store_prices = {
    "sports": 100.0,
    "boots": 120.0,
    "formal": 90.0,
    "casual": 60.0
}

competitor_prices = {
    "sports": 80.0,
    "boots": 140.0,
    "formal": 90.0,
    "casual": 50.0
}

base_demand = {
    "sports": 20,
    "boots": 12,
    "formal": 10,
    "casual": 15
}

result = calculate_market_demand( store_prices, competitor_prices, base_demand, 80)

print("Test : Normal market conditions")
print(result)

assert result == {
    "sports": 18,
    "boots": 15,
    "formal": 11,
    "casual": 13
}
print("Test  passed!")

