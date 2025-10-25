# ROCK PAPER SCISSORS GAME

import random

options = ("Rock", "Paper", "Scissors")
Playing = True

while Playing:
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You win!")
    elif player == "Paper" and computer == "Rock":
        print("You win!")
    elif player == "Scissors" and computer == "Paper":
        print("You win!")
    else:
        print("You Lose!!")

    if not input("Play again? (y/n): ").lower() == "y":
        Playing = False

print("Thanks for Playing!")


