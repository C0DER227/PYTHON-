class Employee:
    company="Google"
    def getSalary(self):
        print(f"The salary for the employee working in{self.company} is:\n{self.salary}")

mukesh=Employee()
mukesh.salary=1000000
mukesh.getSalary()
