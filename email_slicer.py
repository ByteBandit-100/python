#email slicer

email = input("Enter your email : ")

index = email.index('@')
username = email[:index]
domain = email[index+1:]
print(f"The username of email {email} is {username} and domain is {domain}")
