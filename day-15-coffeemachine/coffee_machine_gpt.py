class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # in milliliters
        self.coffee_beans = 200  # in grams
        self.milk = 500  # in milliliters
        self.money = 0  # in dollars

    def display_menu(self):
        print("Menu:")
        print("1. Espresso - $2.50")
        print("2. Latte - $3.00")
        print("3. Cappuccino - $3.50")
        print("4. Check Balance")
        print("5. Exit")

    def make_espresso(self):
        if self.water >= 50 and self.coffee_beans >= 20:
            print("Making Espresso. Enjoy your coffee!")
            self.water -= 50
            self.coffee_beans -= 20
            self.money += 2.50
        else:
            print("Not enough resources to make Espresso. Please refill.")

    def make_latte(self):
        if self.water >= 100 and self.coffee_beans >= 20 and self.milk >= 50:
            print("Making Latte. Enjoy your coffee!")
            self.water -= 100
            self.coffee_beans -= 20
            self.milk -= 50
            self.money += 3.00
        else:
            print("Not enough resources to make Latte. Please refill.")

    def make_cappuccino(self):
        if self.water >= 100 and self.coffee_beans >= 20 and self.milk >= 50:
            print("Making Cappuccino. Enjoy your coffee!")
            self.water -= 100
            self.coffee_beans -= 20
            self.milk -= 50
            self.money += 3.50
        else:
            print("Not enough resources to make Cappuccino. Please refill.")

    def check_balance(self):
        print(f"Current Balance: ${self.money}")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Select an option (1-5): ")

            if choice == '1':
                self.make_espresso()
            elif choice == '2':
                self.make_latte()
            elif choice == '3':
                self.make_cappuccino()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                print("Exiting. Thank you for using the Coffee Machine!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


# Instantiate the CoffeeMachine class and start the program
coffee_machine = CoffeeMachine()
coffee_machine.start()
