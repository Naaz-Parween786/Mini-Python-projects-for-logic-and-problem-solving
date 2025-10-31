# Slot Machine Game: A simple slot machine game where the player can spin to win or lose credits/balance.

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    # Spin the slot machine!
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("***************************")
    print(" | ".join(row)) # join : joins the elements of the list with a space or "|" in between.
    print("***************************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
        
    return 0
    print("No win this time. Better luck next spin!")

    return 0

def main():
    balance = 100  # Starting balance

    print("**********************************")
    print("WELCOME TO THE SLOT MACHINE!")
    print("**********************************")

    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("**********************************")

    while balance > 0:
        print(f"Current Balance: ₹{balance}")
        bet = input("Enter your bet amount : ₹")

        if not bet.isdigit():
            print("Please enter a valid number for your bet.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance for that bet. Try again.")
            continue

        if bet <= 0:
            print("Bet must be greater than zero. Try again.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)
        if payout > 0:
            print(f"Congratulations! You won ₹{payout}!")
            #balance += payout
        else:
            print("No win this time. Better luck next spin!")
            
        balance += payout    

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != 'y':
            break



    print("**********************************")
    print(f"GAME OVER! Your final balance is: ₹{balance}")
    print("**********************************")
            

if __name__ == "__main__":
    main()