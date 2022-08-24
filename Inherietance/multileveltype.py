#multileveltype

class person:
    country="India"
    State="Andhra Pradesh"
    print("I am breathing")

class employee:
    company="GITHUB"
    def getdetails(self):
        print(f"the details are {self.company}")
    def takebreath(self):
        print("I am breathing nd also an employee")

class programmer(employee):
    languauge="PYTHON"
    Company="Microsoft"

p=person()
e=employee()
pr=programmer()
print(p.country)
e.getdetails()
e.takebreath()
pr.takebreath()

    