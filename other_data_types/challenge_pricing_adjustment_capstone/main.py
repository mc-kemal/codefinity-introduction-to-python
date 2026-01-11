grocery_inventory={"Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 5.50, 30),"Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.50, 50)}
egg_information=grocery_inventory.get("Eggs")

egg_price=egg_information[1]

if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    egg_price = egg_price - 1
    grocery_inventory.update({"Eggs": ("Dairy", egg_price, 30)})
else:
    print("The price of Eggs is reasonable.")

grocery_inventory["Tomatoes"]=("Produce", 1.20, 30)

print("Inventory after adding Tomatoes: ", grocery_inventory)

#MANAGE STOCK

milk_information=grocery_inventory.get("Milk")

milk_stock=milk_information[2]

if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    milk_stock = milk_stock + 20
    grocery_inventory.update({"Milk": ("Dairy", 3.50, milk_stock)})
else:
    print("Milk has sufficient stock.")

grocery_inventory["Tomatoes"]=("Produce", 1.20, 30)

print("Inventory after adding Tomatoes: ", grocery_inventory)

#Remove Item Based on Price

apples_information=grocery_inventory.get("Apples")

#print("AInfo: " , apples_information)

apples_price = apples_information[1]

if apples_price > 2:
    print("Apples removed from inventory due to high price.")
    grocery_inventory.pop("Apples")





print("Updated inventory: ", grocery_inventory)
