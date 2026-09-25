import random
from datetime import datetime


def generate_account_number(accounts: dict) -> str:
    """Generates a unique 6-digit account number."""
    while True:
        acc_num = str(random.randint(100000, 999999))
        if acc_num not in accounts:
            return acc_num


def get_current_timestamp() -> str:
    """Returns the current date and time formatted as a string."""
    return datetime.now().strftime("%Y-%m-%d %I:%M %p")


def get_valid_amount(prompt: str) -> float:
    """Prompts the user until a valid positive float amount is entered."""
    while True:
        user_input = input(prompt).strip()
        try:
            amount = float(user_input)
            if amount > 0:
                return amount
            print("⚠️ Amount must be greater than 0. Please try again.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid numerical amount.")


def get_valid_pin(prompt: str) -> str:
    """Prompts the user until a valid 4-digit numeric PIN is entered."""
    while True:
        pin = input(prompt).strip()
        if len(pin) == 4 and pin.isdigit():
            return pin

        print("⚠️ PIN must be exactly 4 numeric digits (e.g., 1234). Please try again.")