# factorial program

number = int(input("Enter a number : "))

def find_factorial(end_number):
    fact = 1
    if end_number < 0 :
        print("Factorial values of negative values cannot defined.")
        return 0
    else :
        for i  in range(1,end_number):
            fact = fact * i
        return fact

if find_factorial(number):
    print(f"The factorial of {number} is : {find_factorial(number+1)}")