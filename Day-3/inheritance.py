class Car:
    def __init__(self, Windows, doors, enginetype):
        self.Windows = Windows
        self.doors = doors
        self.enginetype = enginetype 

    def driving(self):
        print("Car is used for driving")

class Audi(Car):
    def __init__(self, Windows, doors, enginetype, horsepower):
        super().__init__(Windows, doors, enginetype)
        self.horsepower = horsepower

    def selfdriving(self):
        print("It is a self driving car")

audiq7 = Audi(4, 5, "Diesel", 200)

print(audiq7.horsepower)
print(audiq7.Windows)

audiq7.driving()
audiq7.selfdriving()

car1 = Car(4, 5, "Diesel")
print(car1)
print(audiq7)

print(dir(audiq7))
print(dir(car1))