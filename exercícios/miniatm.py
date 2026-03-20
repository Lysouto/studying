"""🏦 The Exercise: "The Mini-ATM"
The Goal: Create a program that starts with a balance of $100. 
The user can choose to Check Balance, Deposit money, Withdraw money, or Exit."""

# Checks if its a valid input
balance = 100
print("Welcome to Mini ATM!")
while True:
    try:
        choice = int(input(
        "Type the number of what you want to do:\n" \
        "1 check balance \n" \
        "2 deposit \n" \
        "3 withdraw \n" \
        "4 exit "))
    except ValueError:
        print("Error. Type a number between 1 and 4 to choose an option ")
        continue
    try:
        if choice == 1:
            print(f"Checking... You currently have ${balance}.")
        elif choice == 2:
            valueadded = float(input("Type the amout to deposit: $"))
            balance += valueadded
        elif choice == 3:
            valuedecreased = float(input("type the amount to withdraw: $"))
            balance -= valuedecreased
            if balance < 0:
                print("You don't have that much money. Transaction cancelled.")
                balance += valuedecreased
                choice2 =input("Do you want to proceed with the transaction knowing you'll be in debt? (y/n) ")
                if choice2 == "y":
                    balance -= valuedecreased
                    print(f"Transaction successful. Your new balance is ${balance}.")
                else:
                    print("Transaction cancelled.")
        elif choice == 4:
            print("Thanks for using Mini ATM. Goodbye!")
            break
        else:
            print("Error. That's not a valid option.")
    except ValueError:
        print("Error. That's not a valid option.")
        continue

# meeh I tried...