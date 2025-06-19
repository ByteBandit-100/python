#greeting according time
# author :: Mohit

import time

_name_ = input("What is your name: ").capitalize()
time = int(time.strftime("%H%M"))

# check greeting conditions.
if (time >= 5 and time <= 1200 ):
    print(f"Hello {_name_} Good morning")

elif (time > 1200 and time <=1600):
    print(f"Hello {_name_} Good afternoon")

elif (time > 1600 and time <=1959):
    print(f"Hello {_name_} Good evening")

else: 
    print(f"Hello {_name_} Good night")