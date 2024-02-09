class MoneyMachine:
    def __init__(self):
        """
        Initialize a MoneyMachine with initial profit.
        """
        self.profit = 0

    def report(self):
        """
        Print the current profit.
        """
        print(f"Money: ${self.profit:.2f}")

    def make_payment(self, cost):
        """
        Accept payment for a drink.

        Parameters:
        - cost (float): The cost of the drink.

        Returns:
        - bool: True when payment is accepted, False if insufficient.
        """
        if cost > 0:
            print(f"Please insert ${cost:.2f}.")
            money_inserted = float(input("How much money are you inserting? $"))
            if money_inserted >= cost:
                change = money_inserted - cost
                self.profit += cost
                print(f"Transaction successful! Here is your change: ${change:.2f}")
                return True
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid cost. Money refunded.")
        return False

# Example usage
money_machine = MoneyMachine()

# Display initial profit
money_machine.report()

# Example cost for a drink
drink_cost = 2.5

# Make a payment
payment_accepted = money_machine.make_payment(drink_cost)

# Display updated profit after making a payment
money_machine.report()
