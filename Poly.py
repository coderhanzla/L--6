class cat:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and I am {self.age} years old....")

    def sound(self):
        print("I can Meow....")

class dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and I am {self.age} years old....")

    def sound(self):
        print("I can Bark....")

class Lion:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and I am {self.age} years old....")

    def sound(self):
        print("I can Roar....")

    
c=cat("Meilow" , 2)
d=dog("Mechiel " , 4)
l=Lion("Shero " , 7)

for animal in (c ,d ,l):
    animal.info()
    animal.sound()
