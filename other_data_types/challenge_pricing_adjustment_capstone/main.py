grocery_inventory={"Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 9.50, 30),"Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.50, 50)}
egg_information=grocery_inventory.get("Eggs")

egg_price=egg_information[1]

if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    egg_price = egg_price - 1
    grocery_inventory.update({"Eggs": ("Dairy", egg_price, 30)})
else:
    print("The price of Eggs is reasonable.")

grocery_inventory[]

#print(egg_price)



#print(grocery_inventory.get("Eggs"))
