import random
import data

class InstagramGame:
    def __init__(self):
        # Load data from external module
        self.data_import = data.data
        # Initialize points counter
        self.points = 0

    def play_round(self):
        # Select random accounts A and B
        account_A = random.choice(self.data_import)
        account_B = random.choice(self.data_import)

        # Ensure that the follower counts of account_A and account_B are different
        while account_B['follower_count'] == account_A['follower_count']:
            account_B = random.choice(self.data_import)

        # Display the options to the user
        print(f"Choice A: {account_A['name']} or B: {account_B['name']} ")

        # Get user input (A or B)
        user_input = input('Who do you think has the highest followers?\nA or B: ').upper()

        # Display follower counts of account A and B
        print(f'Account A: {account_A["follower_count"]} and Account B: {account_B["follower_count"]}')

        # Compare user input with follower counts
        if user_input == 'A':
            if account_A['follower_count'] > account_B['follower_count']:
                print(f'Yes! {account_A["name"]} has the highest followers with {account_A["follower_count"]} followers.')
                self.points += 1
            else:
                print(f'No! {account_B["name"]} has the highest followers with {account_B["follower_count"]} followers.')
        elif user_input == 'B':
            if account_B['follower_count'] > account_A['follower_count']:
                print(f'Yes! {account_B["name"]} has the highest followers with {account_B["follower_count"]} followers.')
                self.points += 1
            else:
                print(f'No! {account_A["name"]} has the highest followers with {account_A["follower_count"]} followers.')
        else:
            print('Invalid input. Please choose A or B.')

        # Display the current points
        print(f'Current points: {self.points}')

    def start_game(self):
        # Flag to control the game loop
        game_on = True

        # Main game loop
        while game_on:
            self.play_round()
            play_again = input('Do you want to play again? (yes/no): ').lower()
            if play_again != 'yes':
                print(f'Game Over! Your final score is: {self.points}')
                game_on = False

# Instantiate the game object and start the game
instagram_game = InstagramGame()
instagram_game.start_game()
