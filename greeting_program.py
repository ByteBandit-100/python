#greeting according time
# author :: Mohit

import time

_name_ = input("What is your name: ").capitalize()
time = int(time.strftime("%H%M"))

# check greeting conditions.
if  5 <= time <=1200:
    print(f"Hello {_name_} Good morning")

elif 1200 < time <=1600:
    print(f"Hello {_name_} Good afternoon")

elif 1600 < time <=1959:
    print(f"Hello {_name_} Good evening")

else: 
    print(f"Hello {_name_} Good night")
