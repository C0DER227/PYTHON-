class employee:
    company="Google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created!")


    def getdetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is{self.salary}")
        print(f"The subunit at which employee work is{self.subunit}")

mukesh= employee("Mukesh",100000,"Nvdia")
mukesh.getdetails()
