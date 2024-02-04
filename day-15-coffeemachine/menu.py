MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    },
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}

# class CoffeeMachine:
#     def __init__(self):
#         self.money = 0  # in dollars

#     def display_menu(self):
#         print("Menu:")
#         for option, details in MENU.items():
#             print(f"{option.capitalize()} - ${details['cost']}")

#     def make_coffee(self, coffee_type):
#         if coffee_type in MENU:
#             ingredients = MENU[coffee_type]['ingredients']
#             cost = MENU[coffee_type]['cost']

#             if all(resources[ingredient] >= ingredients[ingredient] for ingredient in ingredients):
#                 print(f"Making {coffee_type.capitalize()}. Enjoy your coffee!")
#                 for ingredient in ingredients:
#                     resources[ingredient] -= ingredients[ingredient]
#                 self.money += cost
#             else:
#                 print("Not enough resources. Please refill.")
#         else:
#             print("Invalid coffee type. Please choose from the menu.")

#     def check_balance(self):
#         print(f"Current Balance: ${self.money}")

#     def start(self):
#         while True:
#             self.display_menu()
#             choice = input("Select a coffee type or type 'balance' to check balance (type 'exit' to exit): ")

#             if choice.lower() == 'exit':
#                 print("Exiting. Thank you for using the Coffee Machine!")
#                 break
#             elif choice.lower() == 'balance':
#                 self.check_balance()
#             else:
#                 self.make_coffee(choice.lower())

# # Instantiate the CoffeeMachine class and start the program
# coffee_machine = CoffeeMachine()
# coffee_machine.start()
