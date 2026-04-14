"""
Project: The Guessing Game (Higher-Lower)
Goal: A logic-based script where the user guesses a randomly generated number (1-100).
Key Features:
- Dynamic feedback system ("Too high" / "Too low").
- Difficulty (User sets difficulty to play).
- Technical focus: Use of the 'random' module, loop structures, and input sanitization to handle non-numeric guesses.
"""

import random

print("Welcome to the Higher-Lower Game!")

# ask until we get a valid difficulty level
while True:
    try:
        difficulty = int(input("Set a dificulty where \n " \
            "1 is for easy, 2 for medium and 3 for hard: "))
    except ValueError:
        print("Invalid input. Please enter a number 1, 2, or 3.")
        continue

    if difficulty == 1:
        chosen = random.randint(1,10)
        print("Easy selected – number will be between 1 and 10.")
        print(f"(debug) picked {chosen}")  # uncomment to see the actual number
        break
    elif difficulty == 2:
        chosen = random.randint(1,50)
        print("Medium selected – number will be between 1 and 50.")
        break
    elif difficulty == 3:
        chosen = random.randint(1,100)
        print("Hard selected – number will be between 1 and 100.")
        break
    else:
        print("Error. Please choose 1, 2 or 3 and try again.")
        # loop will repeat

guess = 0

while True:
    guess = int(input("Guess the number: "))
    if guess > chosen: 
        print("Guess lower. ")
    elif guess < chosen:
        print("Guess higher. ")
    else:
        print("Congratulations, you've guessed the number!" )
        break
