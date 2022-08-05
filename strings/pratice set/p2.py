letter ='''Dear <|Name|>
     You are selected! 
 <|date|>'''
name=input("enter your name: ")
date=input("Date: ")
letter=letter.replace("<|Name|>",name)  #using replace function changing|name| to name
letter=letter.replace("<|date|>",date)  #using replace function changing |date| to date
print(letter)
