import random
from models.card import Card

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        # Build the deck by combining every suit and rank
        self.cards = [Card(s, r) for s in suits for r in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        # Pop a card off the top of the deck if it's not empty
        if len(self.cards) > 0:
            return self.cards.pop()
        return None