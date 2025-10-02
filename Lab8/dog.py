#Define a class for Dogs:
class Dog:

    #Defines the attributes (properties dogs have) and initializes them:
    #(Attributes are variables that belong to a given class)    
    def __init__(self, name, age, breed, address):
        self.name = name
        self.age = age
        self.breed = breed
        self.address = address

    #Method example:
    def bark(self):
        print(f"{self.name} looks at you and barks: Woof Woof!")
    
    def sleep(self):
         print(f"{self.name} snores loudly, deep asleep.")

    def barkAt(self, barkingAt:str):
        print(f"{self.name} barks loudly at {barkingAt}")

#Create an object from Class Dog:
dog1 = Dog("Bidu", 1, "Mixed", "Kungliga slottet, 107 70 Stockholm")

#Create another object from Class Dog:
dog2 = Dog("Pipoca", 5, "German Sheperd", "Kungliga slottet, 107 70 Stockholm")

dog3 = Dog("Bolt", 5, "American White Shepherd", "Kungliga slottet, 107 70 Stockholm")

dog1.bark()
dog1.barkAt("Carlos")
dog1.sleep()