# Vityarthi-Project
Name: Shorya Khare
Registration Number: 26BAI10804

# Python Blackjack Simulator

# Overview of the Project
Hey! This is a command-line Blackjack game I built entirely in Python. I made this project to simulate the classic casino game where you play against an automated computer dealer, trying to get as close to 21 as possible without busting.

I built this for my Python Essentials course. Instead of just writing one massive script that's impossible to read, I focused heavily on Object-Oriented Programming (OOP). I split the game logic up into separate files for the cards, the deck, the player, and the main game loop. This makes the code way easier to read, scale, and fix if something breaks.

# Features
Multiple Files: The code is split into specific modules (cards.py, deck.py, player.py, dealer.py, and game.py) so every part of the game has its own job.

Real Deck Logic: The program actually builds a 52-card deck, shuffles it using the random module, and handles the drawing mechanics.

Smart Aces: Hand values update in real time. If you draw an Ace and your score gets too high, the game automatically drops the Ace's value from 11 down to 1 so you don't bust.

Dealer AI: The computer plays against you using actual casino rules. It's programmed to keep hitting until its score hits at least 17.

Bank System: I added a virtual wallet that saves your balance to a local JSON file. You can close the game, come back later, and your money will still be there.

Doesn't Crash Easily: I added a bunch of input validation. If you accidentally type a letter instead of a number for your bet, the game catches the error and asks again instead of just crashing the terminal.

# Technologies/Tools Used
Programming Language: Python 3.10+

Standard Libraries: I only used built-in Python tools so you don't have to install anything extra.

random (for shuffling)

json (for saving wallet data)

time (to add small delays so the terminal text doesn't instantly flood the screen)

os (for file paths)

logging (to track errors and game history in the background)

Version Control: Git and GitHub

# Steps to Install & Run the Project

First, just make sure you have Python 3.10 or newer installed on your computer. You don't need to run any pip installs.

Clone the repository by opening your terminal and running:

Bash
git clone https://github.com/adddddme/Vityarthi-Project.git

Navigate into the specific project folder:

Bash

cd Vityarthi-Project/Project

Run the main file to start the game:

Bash

python main.py

# Instructions for Testing

If you want to test the edge cases to see how the code holds up, try doing these things while you play:

The Typo Test: When the game asks you how much you want to bet, type a word like "hello" instead of a number. The try-except block will catch it and ask for a real number.

The Economy Test: Try betting a negative amount or more money than you actually have in your wallet. The game will reject it.

The Ace Shift Test: Watch what happens when you have an Ace in your hand. The game calculates it as 11, but the second your total goes over 21, it instantly recalculates it as a 1.

The Memory Test: Play a few rounds to change your wallet balance, log out, and completely close the terminal window. Run the script again, log in with your same username, and verify your balance carried over.
