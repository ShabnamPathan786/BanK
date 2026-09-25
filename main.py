from auth import create_account, login, change_pin
from transactions import (
    check_balance,
    deposit,
    withdraw,
    transfer,
    view_transaction_history,
)


def user_dashboard(accounts: dict, current_user_acc: str):
    """Displays the user menu for authenticated operations."""
    while True:
        user_name = accounts[current_user_acc]["name"]
        print(f"\n==========================================")
        print(f"🏦 BANKING DASHBOARD | Logged in as: {user_name}")
        print(f"==========================================")
        print("1. 💰 Check Account Balance")
        print("2. ➕ Deposit Money")
        print("3. ➖ Withdraw Money")
        print("4. 🔄 Transfer Money")
        print("5. 📜 View Transaction History")
        print("6. 🔑 Change PIN")
        print("7. 🚪 Logout")
        print("==========================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            check_balance(accounts, current_user_acc)
        elif choice == "2":
            deposit(accounts, current_user_acc)
        elif choice == "3":
            withdraw(accounts, current_user_acc)
        elif choice == "4":
            transfer(accounts, current_user_acc)
        elif choice == "5":
            view_transaction_history(accounts, current_user_acc)
        elif choice == "6":
            change_pin(accounts, current_user_acc)
        elif choice == "7":
            print(f"\n👋 Logged out successfully. Have a great day, {user_name}!")
            break
        else:
            print("⚠️ Invalid choice! Please select an option between 1 and 7.")


def main():
    """Main program entry point."""
    # In-memory storage for all bank accounts
    accounts = {}

    while True:
        print("\n==========================================")
        print("🏦 WELCOME TO PYTHON BANKING SYSTEM")
        print("==========================================")
        print("1. 📝 Create New Account")
        print("2. 🔐 Login to Your Account")
        print("3. ❌ Exit Application")
        print("==========================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            logged_in_acc = login(accounts)
            if logged_in_acc:
                user_dashboard(accounts, logged_in_acc)
        elif choice == "3":
            print("\n🙏 Thank you for banking with us. Goodbye!\n")
            break
        else:
            print("⚠️ Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
