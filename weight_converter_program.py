# weight convertor program 
# kg -> lbs
# lbs -> kg
# author :: Mohit

print("----------x----x----------")

print("Choose K\k for Kilograms(kgs).\nChoose L\l for Pounds(lbs).")
_unit_ = input("In which unit you want to covert weight: ")

if _unit_ == 'k' or _unit_ == 'K':                          #converting pounds(lbs) weight to Kilograms(kgs)
    weight = float(input("Enter weight in lbs: "))
    weight = weight*0.453592
    print(f"The coverted weight is : {weight}Kg") 

elif _unit_ == 'l' or _unit_ == 'L':                        #converting Kilograms(kgs) weight topounds(lbs)
    weight = float(input("Enter weight in kgs: "))
    weight = weight*2.20462
    print(f"The coverted weight is : {weight}Lbs")

else :                                                 #output for if the wrong or empty unit give as an output
    print("The given weight unit is invalid.")

print("----------x----x----------")
