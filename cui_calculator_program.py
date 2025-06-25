#calculator using match case : 
#author : mohit

import time

_name_ = input("What is your name: ").capitalize()
time = int(time.strftime("%H%M"))
_op1_ = 0.0
_op2_ = 0.0
# check greeting conditions.
if  5 <= time <=1200 :
    print(f"Hello {_name_} Good morning")
elif 1200 < time <=1600:
    print(f"Hello {_name_} Good afternoon")
elif 1600 < time <=1959:
    print(f"Hello {_name_} Good evening")
else: 
    print(f"Hello {_name_} Good night")

#function for taking operand input form user
def operand_input():
    global _op1_
    _op1_ = float(input("Enter first value: "))     
    global _op2_
    _op2_ = float(input("Enter second value: "))

if len(_name_.strip())>=2 :                                 #checking user's name 
   while 1:
        print("""---------- MENU --------- \n
1 For Additon( + ) 
2 For Substraction( - ) 
3 For Multiplication( * ) 
4 For Division give( / ) 
5 For Exit 
-->> Press corresponding number for operation.\n""")            #menu for user simplicty to choose operator
        
        _case_ = int(input(f"{ _name_},please give operator: "))


        if _case_:                                  #checks if the operation case input can be given by user

        # match checks the case for operation
            match _case_ :
                case 1:
                    operand_input()
                    print(f"The addition of {_op1_}+{_op2_} is {_op1_ + _op2_}\n")
                case 2:
                    operand_input()
                    print(f"The substraction between {_op1_}-{_op2_} is {_op1_ - _op2_}\n")
                case 3:
                    operand_input()
                    print(f"The multiplication of {_op1_}*{_op2_} is {_op1_ * _op2_}\n")
                case 4:
                    operand_input()
                    print(f"The divison of {_op1_}/{_op2_} is {_op1_ / _op2_}\n")
                case 5:
                    print("You are succefully exit.\n")
                    exit(1)
                case _ :
                    print(f"Oops {_name_} ! The operation is invalid :<  please give any valid operator.\n")

        else:                                                     #if user cannot give any case operator
            print("Please give any operator for operation.\n")

else:                                                              #if name is not possible
    print("Please Re-Execute program & ReEnter your name.\n")