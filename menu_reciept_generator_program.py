menu_items = ('Burger','Pizza','Sandwich','Dessert','Popcorn')
menu_items_price = (8.54,20.32,8.99,17,7)
items = tuple()
x = list(items)
print("menu".upper().center(28))
print('--------------------------------')
print('\tItems'.ljust(9),'|\t Price\t')
print('--------------------------------')
for i in range(len(menu_items)):
    print(f'   {menu_items[i].ljust(8)}  |  ${menu_items_price[i]}')
total_price = 0.0
temp = 0
while 1:
    if temp == 2:
        item = input(f"{item} is not in menu, Please Enter item from menu or q for quit : ").capitalize()
    else:
        item = input("\nEnter an item from menu you want (q for quit) :  ").capitalize()
    for i in range(len(menu_items)):
        if menu_items[i] == item:
            temp = 1
            break
        else:
            temp = 0
    if item.lower() ==  'q':
        print('You are now out from the menu.\n')
        temp = 3
        break
    if temp == 1:
        try:
            count = int(input(f'How many {item} you want : '))
            if count == 1:
                print(f"Your {count}x {item} is added to list.")
            elif count<=0:
                print(f"Count of items not to be zero negative value.Try again to add {item} in list.")
            else:
                print(f"Your {count}x {item}'s are added to list.")
        except:
            print("please re-try and enter count of items in integer format.")
        else:
            for i in range(count):
                x.append(item)
                try:
                    total_price += menu_items_price[menu_items.index(item)]
                except:
                    print('error')
    else:
        temp = 2
if temp==3:
    items = tuple(x)
    print('\tItems'.ljust(10), '  |\t   Price')
    seta = set(items)
    print('------------------------------------')

    for i in seta:
        print(f"{i.ljust(10)} x{items.count(i)}\t|".ljust(15),f" ${menu_items_price[menu_items.index(i)]*items.count(i):.2f}".rjust(10))
    print('------------------------------------')
    print(f"Total price is :",f"${total_price:.2f}".rjust(11))
