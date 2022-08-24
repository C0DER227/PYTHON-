#p3

class employee:
    salary=1000
    increement=1.5
@property
def salaryafterincreement(self):
    return self.salary*self.increement
@salaryafterincreement.setter
def salaryafterincreement(self,sai):
    self.increement=sai/self.salary

e=employee()
print(e.increement)
#print(e.salaryafterincreement)
#e.salaryafterincreement=2000
print(e.increement)