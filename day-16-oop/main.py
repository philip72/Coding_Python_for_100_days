from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from money_machine import MoneyMachine


# Example usage
menu = Menu()

latte_ingredients = {"water": 100, "coffee": 16, "milk": 50}
latte = MenuItem(name="Latte", cost=2.5, ingredients=latte_ingredients)

cappuccino_ingredients = {"water": 100, "coffee": 20, "milk": 30}
cappuccino = MenuItem(name="Cappuccino", cost=3.0, ingredients=cappuccino_ingredients)

expresso_ingredients= {'water': 50,'coffee': 18,}
expresso= MenuItem(name='expresso', cost=1.5, ingredients=expresso_ingredients)
menu.add_item(latte)
menu.add_item(cappuccino)
menu.add_item(expresso)

# Get all menu items
print("Menu Items:", menu.get_items())

# Find a drink by name
order_name = "Cappuccino"
found_item = menu.find_drink(order_name)

if found_item:
    print(f"Found {order_name}:")
    found_item.display_info()
else:
    print(f"{order_name} not found in the menu.")

#coffeemaker

money_machine= MoneyMachine()

money_machine.report()
