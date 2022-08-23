#self
class number:
    def sum(self):
        return self.a + self.b
num=number()
num.a= int(input("Enter the first number:\n"))
num.b= int(input("Enter the secind number:\n"))
s=num.sum()
print("The sum of a and b is:\n",s)
