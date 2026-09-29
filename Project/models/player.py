class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.hand = []

    def draw_card(self, card):
        if card:
            self.hand.append(card)

    def calculate_score(self):
        score = sum(card.get_value() for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == 'Ace')
        
        # If we're busting but have an Ace, drop the Ace's value from 11 to 1
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
            
        return score

    def show_hand(self, hide_dealer_card=False):
        print(f"\n{self.name}'s Hand:")
        for index, card in enumerate(self.hand):
            if index == 1 and hide_dealer_card:
                print(" - [Card Face Down]")
            else:
                print(f" - {card}")
                
        # Only show the score if we aren't hiding the dealer's card
        if not hide_dealer_card:
            print(f"Total: {self.calculate_score()}")