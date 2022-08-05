S=set()
S.add(20)
S.add(20.0)
S.add("20")
print(len(S))             #Prints the length of the set
                          #"20" is a string, 20 = 20.0 in set so it is considered as a unique.

