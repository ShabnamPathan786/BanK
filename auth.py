from utils import (
    generate_account_number,
    get_current_timestamp,
    get_valid_amount,
    get_valid_pin,
)


def create_account(accounts: dict) -> str:
    """Handles new user registration and creates an account."""
    print("\n--- 📝 CREATE NEW BANK ACCOUNT ---")
    name = input("Enter your full name: ").strip()
    phone = input("Enter your phone number: ").strip()

    pin = get_valid_pin("Set a 4-digit PIN: ")

    print("\nInitial deposit is required to activate your account.")
    initial_deposit = get_valid_amount("Enter initial deposit amount ($): ")

    acc_num = generate_account_number(accounts)
    accounts[acc_num] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": initial_deposit,
        "transactions": [
            f"[{get_current_timestamp()}] Account opened with initial deposit: ${initial_deposit:.2f}"
        ],
    }

    print("\n🎉 Account created successfully!")
    print(f"👉 Your Account Number is: {acc_num}")
    print("⚠️ Please save your Account Number and PIN securely.")
    return acc_num


def login(accounts: dict):
    """Authenticates the user using Account Number and PIN."""
    print("\n--- 🔐 ACCOUNT LOGIN ---")
    acc_num = input("Enter your 6-digit account number: ").strip()
    pin = input("Enter your 4-digit PIN: ").strip()

    if acc_num in accounts and accounts[acc_num]["pin"] == pin:
        print(f"\n✅ Welcome back, {accounts[acc_num]['name']}!")
        return acc_num
    else:
        print("\n❌ Invalid Account Number or PIN! Please try again.")
        return None


def change_pin(accounts: dict, current_acc_num: str):
    """Allows the logged-in user to change their PIN."""
    print("\n--- 🔑 CHANGE PIN ---")
    old_pin = input("Enter your current PIN: ").strip()

    if accounts[current_acc_num]["pin"] != old_pin:
        print("❌ Incorrect current PIN! Operation cancelled.")
        return

    new_pin = get_valid_pin("Enter new 4-digit PIN: ")
    confirm_pin = get_valid_pin("Confirm new 4-digit PIN: ")

    if new_pin != confirm_pin:
        print("❌ New PIN and confirmation do not match! PIN not changed.")
        return
    if new_pin == old_pin:
        print("⚠️ New PIN cannot be the same as your old PIN.")
        return

    accounts[current_acc_num]["pin"] = new_pin
    accounts[current_acc_num]["transactions"].append(
        f"[{get_current_timestamp()}] Security: PIN was successfully changed."
    )
    print("✅ PIN has been successfully changed!")
