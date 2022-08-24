#multipletype

class employee:
    company="Flipkart"

class freelancer:
    comanpy="Fiver"
    level=0
    def updradeLevel(self):
     self.level=self.level+1

class programmer(employee,freelancer):
    print("This is a programmer")
p=programmer()
print(p.company)
p.updradeLevel()
print(p.level)