import json


def load_accounts(file_name):
    """Load accounts from a JSON file."""
    try:
        with open(file_name, "r") as file:
            return json.load(file).get("accounts", [])
    except FileNotFoundError:
        return []


def save_accounts(file_name, accounts):
    """Save accounts to a JSON file."""
    with open(file_name, "w") as file:
        json.dump({"accounts": accounts}, file, indent=4)


def create_account(accounts):
    """Create a new account."""
    username = input('Username: ')
    if any(acc['username'] == username for acc in accounts):
        print("Account with this username already exists.")
        return
    password = input('Password: ')
    accounts.append({'username': username, 'password': password, 'balance': 0.0})
    print("Account created successfully!")


def login(accounts, username):
    """Authenticate a user."""
    for account in accounts:
        if account['username'] == username:
            password = input('Enter password: ')
            if password == account['password']:
                print('Login successful!')
                return account
    print('Login failed. Username or password is incorrect.')
    return None


def deposit(account):
    """Deposit money into an account."""
    try:
        amount = float(input('Enter amount to deposit: '))
        if amount > 0:
            account['balance'] += amount
            print(f"Deposit successful! New balance: {account['balance']:.2f}")
        else:
            print("Amount must be greater than 0.")
    except ValueError:
        print("Invalid amount. Please enter a number.")


def withdraw(account):
    """Withdraw money from an account."""
    try:
        amount = float(input('Enter amount to withdraw: '))
        if 0 < amount <= account['balance']:
            account['balance'] -= amount
            print(f"Withdrawal successful! New balance: {account['balance']:.2f}")
        else:
            print("Invalid amount. Check your balance and try again.")
    except ValueError:
        print("Invalid amount. Please enter a number.")


def view_accounts(accounts):
    """View all accounts."""
    print("\n--- Account Details ---")
    for account in accounts:
        print(f"Username: {account['username']}, Balance: {account['balance']:.2f}")
    print("------------------------")


def main():
    file_name = "accounts.json"
    accounts = load_accounts(file_name)

    while True:
        print('\nChoose an option:')
        print('1. Create Account')
        print('2. Login')
        print('3. View All Accounts')
        print('4. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            username = input('Enter username: ')
            user_account = login(accounts, username)
            if user_account:
                while True:
                    print("\n--- Account Menu ---")
                    print('1. Deposit')
                    print('2. Withdraw')
                    print('3. Logout')

                    sub_choice = input('Enter your choice: ')
                    if sub_choice == '1':
                        deposit(user_account)
                    elif sub_choice == '2':
                        withdraw(user_account)
                    elif sub_choice == '3':
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif choice == '3':
            view_accounts(accounts)
        elif choice == '4':
            save_accounts(file_name, accounts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
