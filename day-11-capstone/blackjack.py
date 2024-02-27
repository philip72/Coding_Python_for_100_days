import random

class BlackJack:
    def __init__(self):
        self.cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.points=0
    
    def deal_cards(self):
        random_cards= random.choice(self.cards)

        return random_cards

    def calculate_score(self):
        pass

    def compare(self):
        pass

    def play(self):
        pass
