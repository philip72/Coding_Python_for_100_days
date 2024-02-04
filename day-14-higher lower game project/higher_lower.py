import random
import data

# Load data from external module
data_import = data.data

# Select random accounts A and B
account_A = random.choice(data_import)
account_B = random.choice(data_import)

# Ensure that the follower counts of account_A and account_B are different
if account_B['follower_count'] == account_A['follower_count']:
    account_B = random.choice(data_import)

# Initialize points counter
points = 0

# Flag to control the game loop
game_on = True

# Main game loop
while game_on:
    # Display the options to the user
    print(f"Choice A {account_A['name']} or B {account_B['name']} ")
    
    # Get user input (A or B)
    user_input = input('Who do you think has the highest followers \n A or B ').upper()
    
    # Display follower counts of account A and B
    print(f'account A= {account_A["follower_count"]} and account B {account_B["follower_count"]}')

    # Compare user input with follower counts
    if user_input == 'A':
        if account_A['follower_count'] > account_B['follower_count']:
            print(f'Yes {account_A["name"]} has the highest points {account_A["follower_count"]}')
            points += 1
            # Update account_B for the next round
            account_B = random.choice(data_import)
        else:
            print(f'No {account_B["name"]} has the highest points')
            game_on = False
    elif user_input == 'B':
        if account_A['follower_count'] < account_B['follower_count']:
            print(f'Yes {account_B["name"]} has the highest points {account_B["follower_count"]}')
            points += 1
            # Update account_A for the next round
            account_A = random.choice(data_import)
        else:
            print(f'No {account_A["name"]} has the highest points')
            game_on = False
    else:
        print('Wrong input')
        game_on = False

    # Display the current points
    print(f' Here are the points {points}')
