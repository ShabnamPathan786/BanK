from utils import get_current_timestamp, get_valid_amount


def check_balance(accounts: dict, acc_num: str):
    """Displays the current account balance."""
    balance = accounts[acc_num]["balance"]
    name = accounts[acc_num]["name"]
    print("\n--- 💰 ACCOUNT BALANCE ---")
    print(f"Account Holder : {name}")
    print(f"Account Number : {acc_num}")
    print(f"Current Balance: ${balance:,.2f}")


def deposit(accounts: dict, acc_num: str):
    """Deposits money into the user's account."""
    print("\n--- ➕ DEPOSIT MONEY ---")
    amount = get_valid_amount("Enter amount to deposit ($): ")

    # Update balance
    accounts[acc_num]["balance"] += amount
    new_balance = accounts[acc_num]["balance"]

    # Log the transaction
    timestamp = get_current_timestamp()
    log_entry = f"[{timestamp}] Deposited: +${amount:,.2f} | Balance: ${new_balance:,.2f}"
    accounts[acc_num]["transactions"].append(log_entry)

    print(f"\n✅ Successfully deposited ${amount:,.2f}!")
    print(f"Updated Balance: ${new_balance:,.2f}")


def withdraw(accounts: dict, acc_num: str):
    """Withdraws money after validating available balance."""
    print("\n--- ➖ WITHDRAW MONEY ---")
    current_balance = accounts[acc_num]["balance"]
    print(f"Available Balance: ${current_balance:,.2f}")

    amount = get_valid_amount("Enter amount to withdraw ($): ")

    # Validate sufficient funds
    if amount > current_balance:
        print(f"\n❌ Insufficient funds! You only have ${current_balance:,.2f} available.")
        return

    # Update balance
    accounts[acc_num]["balance"] -= amount
    new_balance = accounts[acc_num]["balance"]

    # Log the transaction
    timestamp = get_current_timestamp()
    log_entry = f"[{timestamp}] Withdrew: -${amount:,.2f} | Balance: ${new_balance:,.2f}"
    accounts[acc_num]["transactions"].append(log_entry)

    print(f"\n✅ Successfully withdrew ${amount:,.2f}!")
    print(f"Remaining Balance: ${new_balance:,.2f}")


def transfer(accounts: dict, sender_acc: str):
    """Transfers money from sender's account to another receiver's account."""
    print("\n--- 🔄 TRANSFER MONEY ---")
    sender_balance = accounts[sender_acc]["balance"]
    print(f"Your Available Balance: ${sender_balance:,.2f}")

    receiver_acc = input("Enter receiver's 6-digit Account Number: ").strip()

    # Edge Case 1: Cannot transfer to own account
    if receiver_acc == sender_acc:
        print("❌ You cannot transfer money to your own account!")
        return

    # Edge Case 2: Receiver account must exist
    if receiver_acc not in accounts:
        print("❌ Receiver account number not found! Please check and try again.")
        return

    amount = get_valid_amount("Enter amount to transfer ($): ")

    # Edge Case 3: Sender must have enough funds
    if amount > sender_balance:
        print(f"\n❌ Transfer failed! Insufficient funds (Available: ${sender_balance:,.2f}).")
        return

    # Perform transfer: deduct from sender, add to receiver
    accounts[sender_acc]["balance"] -= amount
    accounts[receiver_acc]["balance"] += amount

    timestamp = get_current_timestamp()
    sender_name = accounts[sender_acc]["name"]
    receiver_name = accounts[receiver_acc]["name"]

    # Log in sender's account
    sender_log = (
        f"[{timestamp}] Transfer Sent: -${amount:,.2f} to {receiver_name} "
        f"(A/C: {receiver_acc}) | Balance: ${accounts[sender_acc]['balance']:,.2f}"
    )
    accounts[sender_acc]["transactions"].append(sender_log)

    # Log in receiver's account
    receiver_log = (
        f"[{timestamp}] Transfer Received: +${amount:,.2f} from {sender_name} "
        f"(A/C: {sender_acc}) | Balance: ${accounts[receiver_acc]['balance']:,.2f}"
    )
    accounts[receiver_acc]["transactions"].append(receiver_log)

    print(f"\n✅ Successfully transferred ${amount:,.2f} to {receiver_name} (A/C: {receiver_acc})!")
    print(f"Your New Balance: ${accounts[sender_acc]['balance']:,.2f}")


def view_transaction_history(accounts: dict, acc_num: str):
    """Displays all past transactions for the logged-in user."""
    print(f"\n--- 📜 TRANSACTION HISTORY (A/C: {acc_num}) ---")
    transactions = accounts[acc_num]["transactions"]

    if not transactions:
        print("No transactions found for this account.")
        return

    for index, record in enumerate(transactions, start=1):
        print(f"{index}. {record}")
