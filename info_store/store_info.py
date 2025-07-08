print('----- Info Storage ---------')

while True:
    name = input("Enter ur name or q for quit : ")
    if name.lower()=='q':
        break
    age = ''
    mobile =  ''
    try :

        age  = int(input('Enter you age : '))
        mobile = int(input('Enter you mobile number : '))
    except:
        print('invalid input.')
    with open('file1.txt','a+') as fp:
            fp.write(f'\n{name.title().ljust(15)}  {age:2}yrs\t +91{mobile}')