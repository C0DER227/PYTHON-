#P1

class employee:                              #class
    company="Microsoft"
    def __init__(self,name,product):              #constructor
        self.name=name
        self.product=product

    def getdetails(self):                         #obtain details
        print(f"The employee name is {self.name} and the product is {self.product}")

mukesh=employee("Mukesh","Window10")        #assingment
ravi=employee("Ravi","Windows mobile")
nishant=employee("nishant","windows XP")
nitu=employee("nitu","microsoft excel")

mukesh.getdetails()
ravi.getdetails()
nishant.getdetails()
nitu.getdetails()