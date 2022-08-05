#length of string checking using if statements

name=input("Enter the username:\n")
if(len(name)<10):
    print("username contains less than 10 characters")
else:
    print("Username contains more than 10 characters")