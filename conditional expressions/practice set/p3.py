text=input("Enter your statement: \n")

if("make a lot of money" in text):
    spam =True
elif("buy now" in text):
    spam =True
elif("Subscribe this" in text):
    spam = True
elif("Click this" in text):
    spam = True
else:
    spam = False
if(spam):
    print("This is a spam statement")
else:
    print("Statement is not spam")
