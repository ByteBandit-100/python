#Author : ByteBandit-100
#Name   : Mohit

import random

def check(bet_balance,lst):                                 #check wining
    msg = ''
    a = bet_balance
    if lst[0] ==  lst[1] ==  lst[2] == '🍇':
        bet_balance = bet_balance * 8
        msg = f'Wow! Jackpot*8, you won + ${bet_balance}'

    elif lst[0] ==  lst[1] == lst[2] == '🍉':
        bet_balance = bet_balance * 10
        msg = f'Wow! Jackpot*10, you won + ${bet_balance}'

    elif lst[0] ==  lst[1] == lst[2] == '🍌':
        bet_balance = bet_balance * 20
        msg = f'Wow! Jackpot*20, you won + ${bet_balance}'

    else :
        bet_balance = 0
        msg = f'You loss - ${a}'

    return bet_balance,msg

def start(balance):
    if balance<1:
        print(f'Low Balance ${balance}\nPlease try again after you have money.')
    else:
        print(f'\nBalance is : ${balance}')
        bet = 0.0
        try:
            bet = float(input(f'Enter amount you want bet (Current balance : ${balance}) : '))
            if bet < 0:
                print('Invalid input.\nNo -ve money is allowed.')
            elif balance>=bet:
                spin_list = [random.choice(['🍇','🍉','🍌']) for x in range(3) ]
                add_amt,msg = check(bet,spin_list)
                balance += add_amt - bet
                print('*******************')
                print('| ',' | '.join(spin_list),' |')
                print('*******************')
                print(msg,f'\nNow balance : ${balance}')
            else:
                print(f'Oops! The bet amount ${bet} is greater than your balance ${balance}\nTry again.')
        except:
            print('Invalid amount.')
    return balance

def main():
    balance = 20.0
    while True:
        print('------ OPTIONS ------\n')
        print('Enter s for spin.')
        print('Enter q for quit.')
        try:
            option  = input('Enter option s/q : ').lower()
            if option == 'q':
                break

            if option == 's':
                balance = start(balance)
            else:
                print("Invalid input.\nTry Again Later.")
        except:
            print('Please Enter an option.')

if __name__ == '__main__':
    main()