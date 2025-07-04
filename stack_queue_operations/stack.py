stack_lst = []
while True:
    print("--------- Stack --- Menu ---------\n")
    print('''* Stack Works in LIFO manner
stands for Last In First Out 
     
1 for push an item to list
2 for pop an item from list
3 for peak operation of list 
4 for display list
5 for quit 

    ''')
    try:
        user_choice = int(input("Enter choice you want : "))
    except:
        user_choice = 0
    match user_choice:
        case 1:
            x = input("enter value : ")
            stack_lst.append(x)
        case 2: stack_lst.pop() if stack_lst!=[] else print("list is empty.")
        case 3: print(stack_lst[-1]) if stack_lst!=[] else print("list is empty.")
        case 4: print(stack_lst)
        case 5: break
        case _:
            print("Invalid Operation.")