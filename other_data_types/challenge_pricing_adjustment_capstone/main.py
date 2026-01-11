grocery_inventory={"Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 4.50, 30),"Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.50, 50)}
egg_information=grocery_inventory.get("Eggs")

egg_price=egg_information[1]

if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")

#print(egg_price)



#print(grocery_inventory.get("Eggs"))
