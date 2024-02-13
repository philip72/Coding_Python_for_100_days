class CoffeeMaker:
    def __init__(self):
        """
        Initialize a CoffeeMaker with initial resources.
        """
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        """
        Print a report of all resources.
        """
        print("Resources:")
        for resource, amount in self.resources.items():
            print(f"{resource.capitalize()}: {amount}ml/g")

    def is_resource_sufficient(self, drink):
        """
        Check if there are sufficient resources to make a drink.

        Parameters:
        - drink (MenuItem): The MenuItem object to make.

        Returns:
        - bool: True when the drink order can be made, False if ingredients are insufficient.
        """
        for ingredient, amount in drink.ingredients.items():
            if self.resources.get(ingredient, 0) < amount:
                print(f"Sorry, not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, order):
        """
        Deduct the required ingredients from the resources to make a drink.

        Parameters:
        - order (MenuItem): The MenuItem object to make.
        """
        for ingredient, amount in order.ingredients.items():
            self.resources[ingredient] -= amount
        print(f"Enjoy your {order.name}!")

# Example usage
coffee_maker = CoffeeMaker()

# Display initial resources
coffee_maker.report()
from menu import Menu, MenuItem
# Example MenuItem
latte_ingredients = {"water": 200, "coffee": 16, "milk": 150}
latte = MenuItem(name="Latte", cost=2.5, ingredients=latte_ingredients)

# Check if resources are sufficient for the latte
if coffee_maker.is_resource_sufficient(latte):
    coffee_maker.make_coffee(latte)

# Display updated resources after making the latte
coffee_maker.report()
