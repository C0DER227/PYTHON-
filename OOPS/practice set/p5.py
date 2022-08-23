#p5

class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def trainstatus(self):
        print(f"the train number is {self.name} and the seats aviable are {self.seats}")
    def fareInfo(self):
        print(f"the tran fare is Rs.{self.fare}")
    def checkaviability(self):
        if(self.seats>0):
            print(f"Ticket is booked  and availble seats are : {self.seats-1}")
        else:
            print("the train is full try tatkal")
Garibrath=train(15603,120,300)
Garibrath.trainstatus()
Garibrath.fareInfo()
Garibrath.checkaviability()