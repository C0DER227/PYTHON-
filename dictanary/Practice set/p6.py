FavLang={}
a=input("Enter your fav language Abhinav\n")
b=input("Enter your fav language Abhishek\n")
c=input("Enter your fav language Yogesh\n")
d=input("Enter your fav language Rishab\n")

FavLang['Abhinav'] =a
FavLang['Abhishek'] =b
FavLang['Yogesh']   =c                        #if two names are same then recent value will be assinged to the name
FavLang['Rishab']   =d                       #keys must be unique values need not be unique

print(FavLang)
#print(FavLang.keys())     prints names of friends
#print(FavLang.values())   prints the assinged language to them
#print(FavLang.items())    prints total keys & values together 