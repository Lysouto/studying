"""🏦 The Exercise: "The Mini-ATM"
The Goal: Create a program that starts with a balance of $100. 
The user can choose to Check Balance, Deposit money, Withdraw money, or Exit."""

# Starting account balance for the Mini ATM.
balance = 100

# Welcome message shown once when the program starts.
print("Welcome to Mini ATM!")

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
            print(f"Checking... You currently have ${balance:.2f}.")
        elif choice == 2:
            # Option 2: deposit money into the account.
            valueadded = float(input("Type the amout to deposit: $"))
            if valueadded < 0:
                # Prevent negative deposits.
                print("Error. You can't deposit a negative amount.")
                continue
            balance += valueadded
            print(f"Transaction successful. Your new balance is ${balance:.2f}.")
        elif choice == 3:
            # Option 3: withdraw money from the account.
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
                    print(f"Transaction successful. Your new balance is ${balance:.2f}.")
                else:
                    # User cancels the withdrawal, keep the original balance.
                    print(f"Transaction cancelled. Your balance is still ${balance:.2f}.")
            else:
                # Successful withdrawal without overdraft.
                print(f"Transaction successful. Your new balance is {balance:.2f}")
        elif choice == 4:
            # Option 4: exit the program.
            print("Thanks for using Mini ATM. Goodbye!")
            break
        else:
            # Choice outside of the valid menu options.
            print("Error. Type a number between 1 and 4 to choose an option. ")
    except ValueError:
        # Handle invalid numeric conversion during transaction input.
        print("Error. That's not a valid option.")
        continue
