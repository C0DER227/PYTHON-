#single type Inherietance

class employee:
    company="Google"
    def shodetails(self):
        print("This is an Employee")
class programmer(employee):
    language="PYTHON"
    company="GITHUB"
    def getlang(self):
        print(f"The prefered language is {self.language}")
e=employee()
p=programmer()
e.shodetails()
print(e.company)
p.getlang()
print(p.company)
