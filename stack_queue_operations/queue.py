queue_lst = []
while True:
    print("\n--------- Queue --- Menu ---------\n")
    print('''* Queue Works in FIFO manner
stands for First In First Out

1 for push an item to list
2 for pop an item from list
3 for first element of list 
4 for last element of list 
5 for display list
6 for quit 

    ''')
    try:
        user_choice = int(input("Enter choice you want : "))
    except:
        user_choice = 0
    match user_choice:
        case 1:
            x = input("enter value : ")
            queue_lst.append(x)
        case 2:
            if queue_lst != []:
                del queue_lst[0]
            else:
                print("list is empty.")
        case 3:
            print(queue_lst[0]) if queue_lst != [] else print("list is empty.")
        case 4:
            print(queue_lst[-1]) if queue_lst != [] else print("list is empty.")
        case 5:
            print(queue_lst)
        case 6:
            break
        case _ :
            print("Invalid Operation.")
