import random
dice_list = [''' ___________
|           |
|           |
|     •     |
|           |
|___________|''',
''' ___________
|           |
|   •       |
|           |
|       •   |
|___________|
''',
''' ___________
|           |
|   •       |
|     •     |
|       •   |
|___________|
''',
''' ___________
|           |
|   •   •   |
|           |
|   •   •   |
|___________|
''',
''' ___________
|           |
|   •   •   |
|     •     |
|   •   •   |
|___________|
''',
''' ___________
|           |
|   •   •   |
|   •   •   |
|   •   •   |
|___________|
''']
temp = 0
while True:
    user_input = input("-- > q for quit\nHow many dices you want to throw : ")
    if user_input.lower() == 'q':
        break  
    try:
        if int(user_input) != str:
            temp = 1 
    except:
        temp = 0
    if temp:
        user_input = int(user_input)
        if user_input < 1:
            print("The dice throw count is not to be -ve or zero.")
        else:
            total = 0
            for i in range(user_input):
                x = random.randint(0,len(dice_list)-1)
                print(dice_list[x])
                total += x+1
            print(f"Total : {total}")
    else:
        print("Invalid input. Try again :<\n")