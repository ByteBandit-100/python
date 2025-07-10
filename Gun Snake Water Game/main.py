import random
import datetime
dt = datetime.datetime.now().strftime(f'Date:: %Y %b %d\tTime:: %H:%M:%S')
turn = 1
game_opt_dict = {
    'S':'Snake',
    'W':'Water',
    'G':'Gun'
}
user_score =0
computer_score = 0
def check_win(choice,c_choice):
    global user_score,computer_score
    if choice == computer_choice:
        user_score += 1
        computer_score += 1
        return 'Draw'
    elif (choice == 'S' and c_choice == 'W') or (choice == 'W' and c_choice == 'G') or (choice == 'G' and c_choice == 'S'):
        user_score += 1
        return 'Player Win This Round'
    elif (choice == 'W' and c_choice == 'S') or (choice == 'S' and c_choice == 'G') or (choice == 'G' and c_choice == 'W'):
        computer_score += 1
        return 'Computer Win This Round'
usr_name =''
while True:
    if turn == 4 :
        o = input('Want to play again (y for yes/ n for No and quit) : ')
        try :
           o = o.lower().strip()
        except:
            continue
        if o == 'yes' or o =='y':
            turn = 1
            user_score = 0
            computer_score = 0
        elif o == 'no' or o =='n':
            break
        else :
            print('invalid input. ')
            continue
    print('\n--------- Gun Snake & Water ----------')
    print('--> G For Gun.\n--> S for Snake.\n--> W for Water.\n--> Q for Quit.\n--> Case does not matter.\n')
    if turn == 1 and not usr_name:
        usr_name = input('Enter player name : ').capitalize()
    print(f'Round {turn} : ')
    x = input(f'{usr_name} Enter G/S/W (Q for quit) : ')
    computer_choice  = (random.choice(['G','S','W']))
    x = x.upper().strip()
    if x == 'Q':
        break
    if x == 'S' or x == 'W' or x == 'G':
        print(f'\n-------------------------\nPlayer chooses {game_opt_dict[x]}')
        print(f'Computer chooses {game_opt_dict[computer_choice]}\n-->{check_win(x,computer_choice)}\n-------------------------')
        y = f'Result : Player Score   = {user_score}\n'
        z = f'         Computer Score = {computer_score}\n\n--> '
        result = 'Computer Wins\n' if computer_score > user_score else 'Player Wins\n' if computer_score < user_score else 'Draw\n'
        with open('game_data.txt','a') as f:
            if turn == 1:
                f.write(f'\nPlayer : {usr_name}\n')
            f.write(f'Round {turn} :\n')
            f.write(f'\t{usr_name.ljust(15)} : {game_opt_dict[x]}\n{'\tComputer'.ljust(15)}: {game_opt_dict[computer_choice]}\n\n')
            if turn == 3:
                f.write(y+z+result+dt+'\n--------------------- X ---------------------')
        if turn == 3 : print(y+z+result+'-------------------------')
        turn += 1
    else:
        print('invalid input.')