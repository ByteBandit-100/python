# interest calculator

_principle = 0
_interest = 0
_time = 0

while  _principle <= 0 :
    _principle = float(input("Enter principle : "))
    if _principle <= 0 :
        print("Oops!, principle not to be less than or equal to 0.")

while  _interest <= 0 :
    _interest = float(input("Enter interest: "))
    if _interest <= 0 :
        print("Oops!, interest not to be less than or equal to 0.")

while  _time <= 0 :
    _time = float(input("Enter time in year: "))
    if _time <= 0 :
        print("Oops!, time not to be less than or equal to 0.")

total = _principle * pow((1+_interest/100),_time) 

print(f"The total amount is : {total:.2f}")