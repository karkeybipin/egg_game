import json
import os
STORAGE_FILE = "user_data.json"


def load_users():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as file:
            users = json.load(file)
            return users
    return []


def find_user_by_name(name):
    users = load_users()
    for user in users:
        if user['name'].lower() == name.lower():
            return user
    return None


def search_user_by_name():
    name = input("Enter the name to search for: ")
    user = find_user_by_name(name)
    if user:
        print(f"\nAccount Found:")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Account Number: {user['account_number']}")
    else:
        print(f"\nNo account found for the name: {name}")


def menu():
    while True:
        print("\n1. Create User")
        print("2. Display All Users")
        print("3. Search Account by Name")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            display_users()
        elif choice == '3':
            search_user_by_name()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select again.")


def create_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    account_number = generate_account_number()

    user = {
        "name": name,
        "email": email,
        "account_number": account_number
    }

    save_user_details(user)


def generate_account_number():
    return 'AC' + str(random.randint(1000000000, 9999999999))


def save_user_details(user):
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as file:
            users = json.load(file)
    else:
        users = []

    users.append(user)

    with open(STORAGE_FILE, 'w') as file:
        json.dump(users, file, indent=4)

    print(f"User created! Account Number: {user['account_number']}")


def display_users():
    users = load_users()
    if users:
        print("\nStored Users:")
        for user in users:
            print(f"Name: {user['name']}, Email: {
                  user['email']}, Account Number: {user['account_number']}")
    else:
        print("\nNo users found!")


if __name__ == "__main__":
    menu()
