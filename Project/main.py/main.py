import time
from models.deck import Deck
from models.player import Player
from services.bank import Bank
from utils.logger import log_activity

def play_round(player_name, bank):
    deck = Deck()
    user = Player(player_name)
    dealer = Player("Dealer")

    print(f"\n--- Wallet: ${bank.get_wallet(player_name)} ---")
    
    # Keep asking for a bet until they give a valid number
    while True:
        try:
            bet = int(input("How much do you want to bet? $"))
            if 0 < bet <= bank.get_wallet(player_name):
                break
            print("Come on, you can't bet what you don't have (or a negative amount).")
        except ValueError:
            print("Please enter an actual number!")

    print("\nDealing cards...")
    time.sleep(1) # Add a tiny pause for dramatic effect

    # Initial 2 cards each
    user.draw_card(deck.draw())
    dealer.draw_card(deck.draw())
    user.draw_card(deck.draw())
    dealer.draw_card(deck.draw())

    user.show_hand()
    dealer.show_hand(hide_dealer_card=True)

    # User's turn
    while user.calculate_score() < 21:
        move = input("\nDo you want to Hit, Stand, or Double? ").strip().lower()
        
        if move == 'hit':
            user.draw_card(deck.draw())
            user.show_hand()
        elif move == 'stand':
            print("You stand. Let's see what the dealer has...")
            break
        elif move == 'double':
            if bet * 2 <= bank.get_wallet(player_name):
                bet *= 2
                print(f"Bold move! Bet doubled to ${bet}.")
                user.draw_card(deck.draw())
                user.show_hand()
                break
            else:
                print("You don't have enough cash in your wallet to double down.")
        else:
            print("Typo? Type 'hit', 'stand', or 'double'.")

    user_total = user.calculate_score()
    
    # Dealer's turn (only happens if the user didn't already bust)
    if user_total <= 21:
        time.sleep(1)
        print("\n--- Dealer's Turn ---")
        dealer.show_hand()
        time.sleep(1)
        
        while dealer.calculate_score() < 17:
            print("\nDealer hits...")
            time.sleep(1)
            dealer.draw_card(deck.draw())
            dealer.show_hand()

    dealer_total = dealer.calculate_score()

    # Figuring out who won
    time.sleep(1)
    print("\n=== FINAL RESULTS ===")
    
    if user_total > 21:
        print("Ouch, you busted! Dealer wins.")
        bank.change_balance(player_name, -bet)
        log_activity(f"{player_name} lost ${bet} (Busted)")
        
    elif dealer_total > 21:
        print("Dealer busts! You win the hand!")
        bank.change_balance(player_name, bet)
        log_activity(f"{player_name} won ${bet} (Dealer Busted)")
        
    elif user_total > dealer_total:
        print(f"You beat the dealer! {user_total} to {dealer_total}.")
        bank.change_balance(player_name, bet)
        log_activity(f"{player_name} won ${bet} (Higher Hand)")
        
    elif dealer_total > user_total:
        print(f"Dealer wins this round. {dealer_total} to {user_total}.")
        bank.change_balance(player_name, -bet)
        log_activity(f"{player_name} lost ${bet} (Lower Hand)")
        
    else:
        print("It's a push! Tie game.")
        log_activity(f"{player_name} tied.")

def main():
    bank = Bank()
    print("Welcome to Python Casino!")
    
    active_player = None
    
    while True:
        if not active_player:
            print("\n1. Login\n2. Create Account\n3. Walk Away")
            choice = input("What would you like to do? ")
            
            if choice == '1':
                name = input("Username: ")
                if name in bank.accounts:
                    active_player = name
                    print(f"Welcome back, {name}! Let's play.")
                else:
                    print("Never heard of ya. Try making an account first.")
            elif choice == '2':
                name = input("Pick a username: ")
                if bank.create_account(name):
                    print("Account created! Here's $500 on the house. You can log in now.")
                else:
                    print("Someone already took that name.")
            elif choice == '3':
                print("Thanks for stopping by.")
                break
        else:
            print(f"\nMain Menu ({active_player})")
            print("1. Hit the Blackjack Table")
            print("2. Check Wallet")
            print("3. Cash Out (Logout)")
            choice = input("> ")
            
            if choice == '1':
                if bank.get_wallet(active_player) <= 0:
                    print("You're broke! Go wash some dishes.")
                else:
                    play_round(active_player, bank)
            elif choice == '2':
                print(f"You've got ${bank.get_wallet(active_player)} ready to play.")
            elif choice == '3':
                active_player = None

if __name__ == "__main__":
    main()