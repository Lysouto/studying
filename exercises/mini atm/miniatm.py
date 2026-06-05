"""
Project: The Mini-ATM
Goal: A terminal-based banking simulator to practice core programming logic.
Key Features:
- Balance management starting at $100.
- Operations: Check Balance, Deposit, Withdraw, and Exit.
- Technical focus: Input validation, float formatting, and loop control flow.
"""
#Libraries-------------------------------------------------
import math
import json

# Functions and definitions --------------------------------------------------------

def normalize_username(name):
    return name.strip().casefold()

# Create a new user with an unique username
def create_user():
    while True:
        new_user = input("Create a username: ").strip()
        normalized_user = normalize_username(new_user)
        if normalized_user in accounts:
            print("Error. User already exists. Try again. ")
            continue
        else:
            new_pass = input("Create a password: ")
            accounts[normalized_user] = {
                "password": new_pass,
                "balance": 0.0,
                "display_name": new_user
            }
            save_database(accounts)
            print(f"User {new_user} created successfully. you can now Login.")
            break

# Save data whether it's a new user or an updated balance.
def save_database(data):
    with open("exercises/mini atm/registry.json", "w") as file:
              json.dump(data, file, indent=4)

# Welcome message shown once when the program starts.
def welcome_user(user):
    print(f"Welcome to Mini ATM, {user}!")

# Goodbye message shown when the user chooses to exit the program.
def goodbye_user(user):
    print(f"Thanks for using Mini ATM, {user}. Goodbye!")

# Function to display the current balance, formatted to 2 decimal places.
def show_balance(balance):
    print(f"You currently have ${balance:.2f}")

# Function to handle deposits, including input validation for negative amounts.
def deposit(balance):
    valueadded = float(input("Type the amout to deposit: $"))
    if valueadded < 0:
        print("Error. You can't deposit a negative amount.")
        return balance
    balance += valueadded
    print(f"Transaction successful.")
    show_balance(balance)
    return balance

# Function to handle withdrawals, including checks for overdraft and user confirmation if the withdrawal exceeds the current balance.
def withdraw(balance):
    valuedecreased = float(input("type the amount to withdraw: $"))
    balance -= valuedecreased
    if balance < 0:
        # If the withdrawal causes a negative balance, warn the user.
        print("You don't have that much money.")
        balance += valuedecreased
        choice2 = input("Do you want to proceed with the transaction knowing you'll be in debt? (y/n) ")
        if choice2 == "y":
            # User agrees to go into debt, so apply the withdrawal.
            balance -= valuedecreased
            print(f"Transaction successful. ")
            show_balance(balance)
        else:
            # User cancels the withdrawal, keep the original balance.
            print(f"Transaction cancelled. ")
            show_balance(balance)
    else:
        # Successful withdrawal without overdraft.
        print(f"Transaction successful. ")
        show_balance(balance)


# Login state -----------------------------------------------------------------------

# Loading accounts data to read.
with open("exercises/mini atm/registry.json", "r") as file:
    loaded_accounts = json.load(file)

accounts = {}
for username, data in loaded_accounts.items():
    normalized = username.casefold()
    data.setdefault("display_name", username)
    accounts[normalized] = data

# Giving user choice to log in or create a new account:
while True:
    try:
        choicelog = int(input(
        "Type the number of what you want to do:\n" \
        "1 Log in \n" \
        "2 Create account \n" \
        "3 Exit\n"))
    except ValueError:
        # Handle non-numeric menu input.
        print("Error. Type a number between 1 and 3 to choose an option. ")
        continue
    break

if choicelog == 2:
    create_user()
elif choicelog == 3:
    print("Exiting Mini ATM.")
    exit()




# Login existing account loop

# Asks person to type their user:
while True:
    user = input("Type your user to start: ").strip()
    normalized_user = normalize_username(user)

    # 1. Check if the username exists in the accounts database
    if normalized_user in accounts:
        current_user = normalized_user
        password = input("Type your password: ").strip()

        #2 Get the correct password from inside that account
        if password == accounts[current_user]["password"]:

            #3 Get their balance from inside that account
            balance = accounts[current_user]["balance"]

            welcome_user(accounts[current_user].get("display_name", user))
            break
        else:
            print("Incorrect password.")
    else:
        print("User not found. Please try again")
 



# Main loop: keep showing the menu until the user chooses to exit.
while True:
    try:
        # Ask for the user's menu choice and convert to an integer.
        choice = int(input(
        "Type the number of what you want to do:\n" \
        "1 check balance \n" \
        "2 deposit \n" \
        "3 withdraw \n" \
        "4 exit "))
    except ValueError:
        # Handle non-numeric menu input.
        print("Error. Type a number between 1 and 4 to choose an option. ")
        continue

    try:
        if choice == 1:
            # Option 1: display the current balance.
            show_balance(balance)

        elif choice == 2:
            # Option 2: deposit money into the account.
            balance = deposit(balance)
            
            # Update the master dictionary in memory
            accounts[current_user]["balance"] = balance
            # Save the updated master dictionary to the physical file
            save_database(accounts) 

        elif choice == 3:
            # Option 3: withdraw money from the account.
            balance = withdraw(balance)

            # Update the master dictionary in memory
            accounts[current_user]["balance"] = balance
             # Save the updated master dictionary to the physical file
            save_database(accounts)

        elif choice == 4:
            # Option 4: exit the program.
            goodbye_user(user)
            break

        else:
            # Choice outside of the valid menu options.
            print("Error. Type a number between 1 and 4 to choose an option. ")
        
    except ValueError:
        # Handle invalid numeric conversion during transaction input.
        print("Error. That's not a valid option.")
        continue
