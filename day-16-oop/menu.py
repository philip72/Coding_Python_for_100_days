class Menu:
    def __init__(self):
        """
        Initialize a Menu with an empty list to store menu items.
        """
        self.menu_items = []

    def add_item(self, item):
        """
        Add a MenuItem to the menu.

        Parameters:
        - item (MenuItem): The MenuItem to be added to the menu.
        """
        self.menu_items.append(item)

    def get_items(self):
        """
        Get all the names of the available menu items as a concatenated string.

        Returns:
        - str: A string containing the names of all menu items.
        """
        return "/".join(item.name for item in self.menu_items)

    def find_drink(self, order_name):
        """
        Search the menu for a particular drink by name.

        Parameters:
        - order_name (str): The name of the drinks order.

        Returns:
        - MenuItem or None: Returns a MenuItem object if it exists, otherwise returns None.
        """
        for item in self.menu_items:
            if item.name.lower() == order_name.lower():
                return item
        return None

class MenuItem:
    def __init__(self, name, cost, ingredients):
        """
        Initialize a MenuItem with a name, cost, and ingredients.

        Parameters:
        - name (str): The name of the drink.
        - cost (float): The price of the drink.
        - ingredients (dict): The ingredients and amounts required to make the drink.
        """
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

    def display_info(self):
        """
        Display information about the MenuItem.
        """
        print(f"Name: {self.name}")
        print(f"Cost: ${self.cost:.2f}")
        print("Ingredients:")
        for ingredient, amount in self.ingredients.items():
            print(f"  {ingredient}: {amount} units")
            
