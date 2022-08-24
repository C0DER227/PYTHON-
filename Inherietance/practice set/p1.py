#P1
#2d vector and 3d vector

class C2DV:                       #base class
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):       #Dendor __str__
        return f"{self.icap}i+{self.jcap}j"

class C3DV(C2DV):               #inheritance #Derived 
    def __init__(self, i, j, k):
        self.icap=i
        self.jcap=j
        self.kcap=k
        super().__init__(i, j) #obtaining from base class
    def __str__(self):          #Dendor __str__
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"

C2DV=C2DV(1,3)
C3DV=C3DV(1,9,7)
print(C2DV)
print(C3DV)