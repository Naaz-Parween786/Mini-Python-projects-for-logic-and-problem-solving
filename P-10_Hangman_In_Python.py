# Hangman Game: A simple hangman game where the player has to guess the word letter by letter.
# The player has a limited number of attempts to guess the word correctly.

from wordslist import words
import random

# dictionary to hold hangman stages: ()

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: ("  o  ",
                   " /|  ",
                   "     "),
               4: ("  o ",
                   " /|\\",
                   "   "),
               5: ("  o  ",
                   " /|\\ ",
                   " /  "),
               6: ("  o ",
                   " /|\\",
                   " / \\"),                       
             }

def display_man(wrong_guesses):
    print("--------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("--------------------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))
    

def main():
    answer = random.choice(words)
    # print(answer)  # For testing purposes, remove or comment this line in production.
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess)!= 1 or not guess.isalpha():
            print("Invalid Input!! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)





        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {6 - wrong_guesses} attempts left.")
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(hint)
            print("You Won!! You guessed the word correctly!")

            is_running = False
        
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print(f"Game Over! The correct word was '{answer}'.")   
            print("You Lose! Better luck next time!")
            is_running = False


if __name__ == "__main__":
    main()









