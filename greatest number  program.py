# greatest number betweeen three numbers
# author :: Mohit

# import math

_num1 = int(input("Enter 1st value: "))
_num2 = int(input("Enter 2nd value: "))
_num3 = int(input("Enter 3rd value: "))

if _num1 != _num2 != _num3 :
    if _num1 > _num2 :
        if _num1 > _num3 :
            print("The greatset value is: ",_num1)
        else :
            print("The greatset value is: ",_num3)
    else :
        if _num2 > _num3 :
            print("The greatset value is: ",_num2)
        else :
            print("The greatset value is: ",_num3)
            
    # #or
    # print("The greatest value is: ",max(_num1,_num2,_num3))

else :
    print(f"{_num1} = {_num2} = {_num3} are same.")
