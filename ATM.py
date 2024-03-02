import sys

account_balance = float(500.25)

def print_balance():
    return account_balance

def deposit_amount(amount):
    global account_balance
    account_balance += amount
    return account_balance

def withdrawal_amount(amount):
    global account_balance
    if amount > account_balance:
        print('$%.2f is greater than your account balance of $%.2f' % (amount, account_balance))
    else:
        account_balance -= amount
    return account_balance

def display_menu():
    print("Menu:")
    print("B - Check Balance")
    print("D - Deposit")
    print("W - Withdrawal")
    print("Q - Quit")

def main():
    while True:
        display_menu()
        userchoice = input("What would you like to do?\n").upper()

        if userchoice == 'B':
            print('Your current balance: $%.2f' % print_balance())
        elif userchoice == 'D':
            deposit = float(input('How much would you like to deposit today?\n'))
            account_balance = deposit_amount(deposit)
            print('Deposit was $%.2f, current balance is $%.2f' % (deposit, account_balance))
        elif userchoice == 'W':
            withdrawal = float(input('How much would you like to withdraw today?\n'))
            account_balance = withdrawal_amount(withdrawal)
            if account_balance is not None:
                print('Withdrawal amount was $%.2f, current balance is $%.2f' % (withdrawal, account_balance))
        elif userchoice == 'Q':
            print('Thank you for banking with us. Goodbye!')
            break
        else:
            print('Invalid choice. Please select a valid option.')

        return_to_menu = input('Would you like to return to the main menu? (Y/N)\n').upper()
        if return_to_menu != 'Y':
            print('Thank you for banking with us. Goodbye!')
            break

if __name__ == "__main__":
    main()



