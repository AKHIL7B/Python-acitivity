units = float(input("Number of units produced: "))
material_per_unit = float(input("Material cost per unit: "))
wastage_percent = float(input("Wastage percentage of material: "))
labour_hours = float(input("Labour hours: "))
labour_rate = float(input("Labour rate per hour: "))
machine_cost = float(input("Machine cost: "))
selling_price = float(input("Selling price per unit: "))
target_percent = float(input("Target profit percentage: "))

material = units * material_per_unit
wastage = material * wastage_percent / 100
labour = labour_hours * labour_rate
total_cost = material + wastage + labour + machine_cost
revenue = units * selling_price
profit = revenue - total_cost
profit_percent = profit / total_cost * 100

print(f"Material cost : {material:.2f}")
print(f"Wastage cost  : {wastage:.2f}")
print(f"Labour cost   : {labour:.2f}")
print(f"Machine cost  : {machine_cost:.2f}")
print(f"Total cost    : {total_cost:.2f}")
print(f"Revenue       : {revenue:.2f}")
print(f"Profit        : {profit:.2f}")
print(f"Profit %      : {profit_percent:.2f}%")

if profit_percent >= target_percent:
    print("Result: profit target is met.")
else:
    print(f"Result: Profit target is not met. Short by {target_percent - profit_percent:.2f} percentage points.")