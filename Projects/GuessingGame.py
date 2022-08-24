#GUESSING GAME

import random
randnumber=random.randint(1,100)  #to keep it fair we are not printing randnumber
userguess=None
guesses=0
while(userguess!=randnumber):
    userguess=int(input("Enter your guess:"))
    guesses+=1
    if(userguess==randnumber):
        print("You guessed it Rightly Hurray!!!")
    else:
        if(userguess>randnumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
print(f"You guessed the number in {guesses}guesses")

#for highscore storage
'''with open("Hiscore.txt","r")as f:
    Hiscore=int(f.read())

if(guesses<Hiscore):
    print("You have just broken the Record!!!!")
    with open("Hiscore.txt","w")as f:
        f.write(str(guesses))'''

