#find my marks calculator program

marks = float(input("Enter marks between 0-100 : "))

if  85 <= marks < 100 :
    print("Wow! you got 'A' Grade.")
elif 68 <= marks < 85:
    print("Good,  you got 'B' Grade.")
elif 50 <= marks < 68:
    print("Its fine, you got 'C' Grade.")
elif 46 <= marks < 50:
    print("Keep it up, you got 'D' Grade.")
elif 30 <= marks < 45:
    print("You need more hard work, you got 'F' Grade.")
elif marks < 0 or marks >100:
    print("Marks not be negative or greater than 100.")
else:
    print("You Fail this time, You need hard work.")