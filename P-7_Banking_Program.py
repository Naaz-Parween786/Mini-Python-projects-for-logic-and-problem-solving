# Python Banking Program:-


def show_balance(balance):
    print("**********************************")
    print(f"Your current balance is: ₹{balance}")
    print("**********************************")

def deposit():
    print("**********************************")
    amount = float(input("Enter amount to deposit: ₹"))
    print("**********************************")

    if amount < 0:
        print("**********************************")
        print("Invalid!Deposit amount cannot be negative.")
        print("**********************************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("**********************************")
    amount = float(input("Enter amount to withdraw: ₹"))
    print("**********************************")
    if amount > balance:
        print("**********************************")
        print("Insufficient funds! Cannot withdraw more than the current balance.")
        print("**********************************")
        return 0
    elif amount < 0:
        print("**********************************")
        print("Invalid! Withdraw amount cannot be negative.")
        print("**********************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("**********************************")
        print("BANKING PROGRAM")
        print("**********************************")
        

        print("1. Show Balance")
        print("2.Ddeposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance +=deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
            print("Exiting the program...Goodbye!")
        else:
            print("**********************************")
            print("Invalid choice. Please try again.")
            print("**********************************")
    print("**********************************")
    print("Thank you for using the Banking Program. Have a great day!")
    print("**********************************")

if __name__ == "__main__":
   main()














