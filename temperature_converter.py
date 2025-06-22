# program for converting temperature 
# farnheit -> celcius 
# celcius  -> farnheit
# author :: Mohit

print("----------x----x----------")

print("Choose C\c for Celcius.\nChoose F\\f for farnheit.")
_unit_ = input("In which unit you want to convet the temperature:")

if _unit_ == 'C' or _unit_ == 'c':                                          #conveting farnheit to celcius
    temperature = float(input("Enter temperature value in farnheit: "))
    temperature = (temperature - 32) * (5/9) 
    print(f"The temperature in Celcius is : {temperature}C")

elif _unit_ == 'F' or _unit_ == 'f':                                         #conveting celcius to farnheit
    temperature = float(input("Enter temperature value in celcius: "))
    temperature = temperature * (9/5) + 32
    print(f"The temperature in Farnheit is : {temperature}F")

else :                                                                       #output for if the wrong or empty unit give as an output
    print("The given temperature unit is invalid.")

print("----------x----x----------")
