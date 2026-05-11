"""
Project: The Mini-ATM
Goal: A terminal-based banking simulator to practice core programming logic.
Key Features:
- Balance management starting at $100.
- Operations: Check Balance, Deposit, Withdraw, and Exit.
- Technical focus: Input validation, float formatting, and loop control flow.
"""
import math

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

# Login state

# User accounts with their respective balances (for future expansion).
accounts = {
    "gamer": 100.00,
    "user2": 150.00,
    "admin": 9999.00
}

passwords ={
    "gamer": "password123",
    "user2": "password456",
    "admin": "password789"
}

# Starting account balance for the Mini ATM.
balance = 100

# Asks person to type their user. 
user = input("Type your user to start: ")

if user in accounts:
    current_user = user
    password = input("Type your password: ")
    # In a real application, you would check the password here.
    if password == passwords[current_user]:  # Replace with actual password checking logic
        balance = accounts[current_user]
        welcome_user(current_user)
    else:
        print("Incorrect password.")
else:
    print("User not found. Starting with a default balance of $100.")
    current_user = user
    welcome_user(current_user)
    



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
        elif choice == 3:
            # Option 3: withdraw money from the account.
            balance = withdraw(balance)
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
