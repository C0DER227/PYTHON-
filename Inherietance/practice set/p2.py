#P2

class animals:
    type="Mamels"

class pet(animals):
    color="White"

class dog(pet,animals):
    @staticmethod
    def bark():
     print("!!!!!BOW BOW!!!!")

d=dog()
d.bark()