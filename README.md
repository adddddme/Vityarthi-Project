# Vityarthi-Project
# Project Title: Python Blackjack Simulator
#Overview of the Project
This project is a command-line Blackjack game built natively in Python. It is designed to simulate the classic casino card game where a player competes against an automated dealer to build a hand as close to 21 as possible without busting. The project demonstrates core computer science and Object-Oriented Programming (OOP) concepts, separating responsibilities into multiple distinct modules (such as cards, decks, players, and game logic) to ensure a clean, maintainable, and scalable architecture.

#Features
Modular Architecture: Codebase divided into specific modules (cards.py, deck.py, player.py, dealer.py, game.py) for clean separation of concerns.

Dynamic Deck Management: Programmatic generation of a standard 52-card deck with automated shuffling and drawing mechanics.

Advanced Score Calculation: Real-time evaluation of card values, including dynamic handling of Aces (automatically converting values from 11 to 1 to prevent a player from busting).

Automated Dealer AI: A computer-controlled dealer that strictly follows standard casino rules (drawing until a score of 17 is reached).

Persistent User Economy: A virtual bank system that tracks player balances across multiple sessions using JSON file storage.

Robust Error Handling: Continuous input validation to prevent the application from crashing due to unexpected user inputs (e.g., typing letters instead of bet amounts).

# Technologies/Tools Used
Programming Language: Python 3.10+

Standard Libraries:

random (for deck shuffling)

json (for reading and writing persistent wallet data)

time (for pacing terminal outputs)

os (for directory and file path management)

logging (for tracking game events and errors)

Version Control: Git and GitHub

# Steps to Install & Run the Project
Prerequisites: Ensure Python 3.10 or newer is installed on your system. No external libraries or pip installations are required.

Clone the Repository:
Open your terminal or command prompt and run:

Bash
git clone 
Navigate to the Directory:

Bash
cd game.black_jack
Run the Game:
Execute the main Python script to launch the command-line interface:

Bash
python main.py
Instructions for Testing
To verify the system functions correctly, perform the following integration tests during runtime:

# Instructions for Testing
To verify the system functions correctly, perform the following integration tests during runtime:

Input Validation Test: When prompted to enter a bet amount, type alphabetical characters (e.g., "abc") instead of a number. The system should catch the error and prompt you again without crashing the program.

Economy Test: Attempt to bet an amount greater than your current wallet balance or a negative number. The system should reject the bet.

Ace Logic Test: Monitor hands containing an Ace. Ensure the system correctly evaluates the Ace as 11, but automatically drops its value to 1 if drawing another card pushes the total score over 21.

Persistence Test: Play a round, log out of the game, and restart the terminal completely. Log back in with the same username to verify your wallet balance was saved correctly.
