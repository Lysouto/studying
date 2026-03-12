"""🎮 The Exercise: "The Higher-Lower Game"
The Goal: Write a script where the computer picks a random number between 1 and 100,
and the player has to guess it. The computer should tell them if their guess is "Too high" 
or "Too low" until they get it right."""

import random
chosen = random.randint(1,100)
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
