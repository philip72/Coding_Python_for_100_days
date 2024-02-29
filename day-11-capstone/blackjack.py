import random

class BlackJack:
    def __init__(self):
        self.cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.points=0
    
    def deal_cards(self):
        random_cards= random.choice(self.cards)

        return random_cards

    def calculate_score(self, cards):
        self.cards=cards
        if sum(cards)==21 and len(cards)==2:
            return 0
        if sum(cards)>21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(self, user_score, computer_score):
        """Compare the scores and determine the winner."""
        self.user_score=user_score
        self.computer_score=computer_score
        if user_score == computer_score:
            return "It's a draw."
        elif computer_score == 0:
            return "Computer has Blackjack. You lose."
        elif user_score == 0:
            return "You have Blackjack. You win!"
        elif user_score > 21:
            return "You went over. You lose."
        elif computer_score > 21:
            return "Computer went over. You win!"
        elif user_score > computer_score:
            return "You win!"
        else:
            return "You lose."

    def play(self):
        user_cards=[self.deal_cards(), self.deal_cards()]
        computer_cards=[self.deal_cards(),self.deal_cards()]
        game_over=False

        while not game_over:
            user_score=self.calculate_score(user_cards)
            computer_score=self.calculate_score(computer_cards)

            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                game_over = True
            else:
                should_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()
                if should_continue == 'y':
                    user_cards.append(deal_card())
                else:
                    game_over = True
        while computer_score !=0 and computer_score<17 :
            computer_cards.append(self.deal_cards())
            computer_score=self.calculate_score(computer_cards)
        
        print(f" Your final hand: {user_cards}, final score: {user_score}")
        print(f"computer's final hand:  {computer_cards}, final score: {computer_score}")
        print(self.compare(user_score, computer_score))


