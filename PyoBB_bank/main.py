def menu():
    print('\n-------- PyoBB Bank --------')
    print('1 for Show Balance.\n2 for Deposit money. \n3 for Withdraw money.\n4 for quit the loop.\n')
    choice  = input('Enter choice : ')
    return choice

def show_balance(balance):
    print(f'Your Current Balance is : ${balance}')

def deposit_money(balance):
    try:
        deposit_amt = float(input('Enter the amount you want to deposit in $ : '))
        if deposit_amt >0:
            balance += deposit_amt 
            show_balance(balance)
            return balance  
        else:
            print('value does not 0 or -ve')
            return balance
    except:
        print('Retry and enter valid amount.')
        return balance

def withdraw_money(balance):
    try:
        withdraw_amt = float(input('Enter amount you want to withdraw in $ : '))
        if withdraw_amt < balance:
            if withdraw_amt <= 0  :
                print('Value does not 0 or -ve. ')
                return balance
            else:
                balance -= withdraw_amt
                show_balance(balance)
                return balance
        else:
            print(f'Your current balance {balance} is not sufficient amount to withdraw amount {withdraw_amt}')
            return balance
    except:
        print('Retry and enter valid amount.')
        return balance

def main():
    balance = 0.0
    while True:
        usr_choice = menu()
        match usr_choice :
            case '1' : show_balance(balance)
            case '2' : balance = deposit_money(balance)
            case '3' : balance = withdraw_money(balance)
            case '4' : break
            case _   : print(f'Your input {usr_choice} is not valid.\nTry again.')

if __name__ == '__main__':
    main()