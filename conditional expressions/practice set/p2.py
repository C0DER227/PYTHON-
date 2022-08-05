Sub1=int(input("Enter the marks of subject 1: "))
Sub2=int(input("Enter the marks of subject 2: "))
Sub3=int(input("Enter the marks of subject 3: "))
if(Sub1<33 or Sub2<33 or Sub3<33):
    print("You failed because one of the subject you got less marks")
if(((Sub1+Sub2+Sub3)/3) <40):
    print("You failed becoz u got less overall total")
else:
    print("!!!!!!!Congratulations, you passed wit flying colours!!!!!!!!!!!")
