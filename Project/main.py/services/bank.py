import json
import os
from utils.logger import log_activity, log_error

DB_FILE = 'data/players.json'

class Bank:
    def __init__(self):
        self.accounts = self.load_data()

    def load_data(self):
        # If it's the first time running, the file won't exist yet
        if not os.path.exists(DB_FILE):
            return {}
        try:
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            log_error(f"Couldn't load player data: {e}")
            return {}

    def save_data(self):
        try:
            with open(DB_FILE, 'w') as f:
                json.dump(self.accounts, f, indent=4)
        except Exception as e:
            log_error(f"Couldn't save player data: {e}")

    def create_account(self, username):
        if username in self.accounts:
            return False # User already exists
            
        # Give newbies a $500 starting bonus
        self.accounts[username] = {"wallet": 500} 
        self.save_data()
        log_activity(f"New player registered: {username}")
        return True

    def get_wallet(self, username):
        return self.accounts.get(username, {}).get("wallet", 0)

    def change_balance(self, username, amount):
        if username in self.accounts:
            self.accounts[username]["wallet"] += amount
            self.save_data()