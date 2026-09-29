import logging
import os

# Create the data folder if it doesn't exist yet
os.makedirs("data", exist_ok=True)

# Set up a basic logger to keep track of wins/losses and errors
logging.basicConfig(
    filename='data/game_history.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def log_activity(message):
    logging.info(message)

def log_error(message):
    logging.error(message)