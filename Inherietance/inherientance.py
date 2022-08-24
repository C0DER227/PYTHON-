#inherientance

class employee:
    company="Amazon"
    def employeeInfo(self):
        print("This is an Employee")
class programmer(employee):
    language="PYTHON"

    def getLangInfo(self):
        print(f"The language is {self.language}")

    def programmerInfo(self):
        print("This is an Programmer")
e=employee()
p=programmer()
e.employeeInfo()
p.programmerInfo()