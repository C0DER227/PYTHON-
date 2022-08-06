#remove and strip a string:

def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
this="     mukesh is good  "
n= remove_and_split(this,"mukesh")
print(n)