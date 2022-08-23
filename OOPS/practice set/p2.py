#P2

class calculator:
    def __init__(self,num):                       #constructor
        self.num=num

    def square(self):                            #square declaration
        print(f"the square of {self.num} is {self.num**2}")

    def squareroot(self):                         #sqaureroot declaration
        print(f"the sqaureroot of {self.num} is {self.num**0.5}")

    def cube(self):                                #cube declaration
        print(f"the cube of {self.num} is {self.num**3}")
        
a=calculator(int(input("Enter the number: ")))
a.square()
a.squareroot()
a.cube()
