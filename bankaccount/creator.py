import json
import os
STORAGE_FILE = "bank_accounts.json"


def load_users():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as file:
            users = json.load(file)
            return users
    return []


def save_users(users):
    with open(STORAGE_FILE, 'w') as file:
        json.dump(users, file, indent=4)


def create_account():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    account_number = generate_account_number()
    balance = 0.0
    user = {
        "name": name,
        "email": email,
        "account_number": account_number,
        "balance": balance
    }

    users = load_users()
    users.append(user)
    save_users(users)

    print(f"Account created successfully! Account Number: {account_number}")
    print(f"Starting Balance: ${balance:.2f}")


def generate_account_number():
    return 'AC' + str(random.randint(1000000000, 9999999999))


def find_user_by_account_number(account_number):
    users = load_users()
    for user in users:
        if user['account_number'] == account_number:
            return user
    return None


def deposit():
    account_number = input("Enter your account number: ")
    user = find_user_by_account_number(account_number)

    if user:
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            user['balance'] += amount
            save_users(load_users())
            print(f"Deposited ${amount:.2f} successfully. New balance: ${
                  user['balance']:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")
    else:
        print("Account not found.")


def withdraw():
    account_number = input("Enter your account number: ")
    user = find_user_by_account_number(account_number)

    if user:
        amount = float(input("Enter amount to withdraw: $"))
        if amount > 0 and amount <= user['balance']:
            user['balance'] -= amount
            save_users(load_users())
            print(f"Withdrew ${amount:.2f} successfully. Remaining balance: ${
                  user['balance']:.2f}")
        elif amount > user['balance']:
            print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a positive number.")
    else:
        print("Account not found.")


def display_balance():
    account_number = input("Enter your account number: ")
    user = find_user_by_account_number(account_number)

    if user:
        print(f"Account Holder: {user['name']}")
        print(f"Account Number: {user['account_number']}")
        print(f"Current Balance: ${user['balance']:.2f}")
    else:
        print("Account not found.")


def menu():
    while True:
        print("\n------ Bank Application ------")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            display_balance()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
