# Project Statement
# Problem Statement
Building a robust digital card game requires a solution for simulating real-time probabilistic outcomes and securely managing application state under constrained rulesets. The objective of this project is to develop a modular, object-oriented simulation of Blackjack that manages persistent user data, handles edge-case logic (such as variable Ace values), and strictly enforces game rules in a command-line environment without crashing due to unexpected inputs.

# Scope of the Project
The scope of this project is restricted to a local command-line interface (CLI) application

Included:

A user authentication system and local JSON-based wallet for tracking virtual currency.

A standard 52-card deck randomization and drawing algorithm.Turn-based logic against an automated, computer-controlled dealer.

Background system logging for runtime events and errors.

Excluded:

Real-money transactions or actual gambling.

Graphical User Interfaces (GUI) or mobile application functionality.

Internet-based multiplayer, web servers, or online leaderboards.

# Target Users

Computer Science Students: Individuals studying Object-Oriented Programming (OOP), state management, and file I/O operations who need a practical, readable codebase to reference. 

Python Beginners: Learners seeking to understand how basic syntax (loops, functions, dictionaries) is combined to build a functional, multi-module application.  

Casual Gamers: Users looking for a lightweight, terminal-based probability game that requires no external libraries or internet connection.

# High-Level Features

Persistent User Ledger: A registration and login system that securely reads and writes virtual currency balances to a local data store across multiple sessions.

Dynamic Game Engine: Calculates real-time card values, manages virtual bets, and dynamically scales Ace cards (between 1 and 11) to prevent structural overloads (busts). 

Automated Opponent: A dealer algorithm that automatically evaluates its hand and draws cards based on standard casino thresholds (hitting until a score of 17 is reached).

Input Validation & Error Handling: Continuous validation of user keystrokes to ensure invalid data types (like alphabetical text entered during an integer bet prompt) are caught and handled safely without terminating the program. 
