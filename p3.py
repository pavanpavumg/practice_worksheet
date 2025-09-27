# 🏦 Simple Banking System (Beginner Version)

# Dictionaries to store data
customers = {}       # {acc_no: [name, age, type, balance]}
transactions = {}    # {acc_no: [list of transactions]}
MIN_BALANCE = 1000   # Minimum balance warning

# Create a new account
def create_account():
    acc_no = input("Enter new account number: ")
    if acc_no in customers:
        print("❌ Account already exists!\n")
        return
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    acc_type = input("Enter Account Type (Saving/Current): ")
    balance = float(input("Enter Initial Balance: "))

    # Save account details
    customers[acc_no] = [name, age, acc_type, balance]
    transactions[acc_no] = [f"Account created with balance {balance}"]

    print("✅ Account created successfully!\n")

# Deposit money
def deposit():
    acc_no = input("Enter Account Number: ")
    if acc_no not in customers:
        print("❌ Account not found.\n")
        return
    amount = float(input("Enter amount to deposit: "))
    customers[acc_no][3] += amount
    transactions[acc_no].append(f"Deposited {amount}")
    print("💰 Deposit successful!\n")

# Withdraw money
def withdraw():
    acc_no = input("Enter Account Number: ")
    if acc_no not in customers:
        print("❌ Account not found.\n")
        return
    amount = float(input("Enter amount to withdraw: "))
    if customers[acc_no][3] >= amount:
        customers[acc_no][3] -= amount
        transactions[acc_no].append(f"Withdrew {amount}")
        print("💸 Withdrawal successful!\n")
    else:
        print("❌ Insufficient balance.\n")

# Check balance
def check_balance():
    acc_no = input("Enter Account Number: ")
    if acc_no not in customers:
        print("❌ Account not found.\n")
        return
    balance = customers[acc_no][3]
    print(f"💳 Current Balance: {balance}")
    if balance < MIN_BALANCE:
        print("⚠️ Warning: Balance is below minimum!\n")

# Transfer money between two accounts
def transfer():
    from_acc = input("Enter FROM Account: ")
    to_acc = input("Enter TO Account: ")
    if from_acc not in customers or to_acc not in customers:
        print("❌ One or both accounts not found.\n")
        return
    amount = float(input("Enter amount to transfer: "))
    if customers[from_acc][3] >= amount:
        customers[from_acc][3] -= amount
        customers[to_acc][3] += amount
        transactions[from_acc].append(f"Transferred {amount} to {to_acc}")
        transactions[to_acc].append(f"Received {amount} from {from_acc}")
        print("✅ Transfer successful!\n")
    else:
        print("❌ Insufficient balance in source account.\n")

# View all customers
def view_customers():
    if not customers:
        print("No customers found.\n")
        return
    print("\n--- Customer List ---")
    for acc_no, details in customers.items():
        name, age, acc_type, balance = details
        print(f"Acc No: {acc_no} | Name: {name} | Age: {age} | Type: {acc_type} | Balance: {balance}")
    print()

# View transaction history
def view_transactions():
    acc_no = input("Enter Account Number: ")
    if acc_no not in transactions:
        print("❌ Account not found.\n")
        return
    print(f"\n📜 Transactions for {acc_no}:")
    for txn in transactions[acc_no]:
        print("-", txn)
    print()

# Main menu
def main():
    while True:
        print("\n===== Banking Menu =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. View Customers")
        print("7. View Transactions")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            transfer()
        elif choice == '6':
            view_customers()
        elif choice == '7':
            view_transactions()
        elif choice == '8':
            print("👋 Thank you for using the Banking System!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Run program
main()


main()
