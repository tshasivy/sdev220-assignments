#Author:  Tejas Shastri
#Program name: Vehicle Class 
#Filename: M03Lab.py
#Date: 11/12/2023
#Description: Utilizing a super class and a class, this program implements a system that collects vehicle information and displays it.




class Vehicle():
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):  #This class extends Vehicle()
    def __init__(self, vehicleType, year, make, model, doors, roof):
        super().__init__(vehicleType)

        #These are the attributes not found in Vehicle()
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#Implementing a while loop to repeat process
car = input("Is your vehicle a car? Type Yes to continue or No to quit: ")
while(car=="Yes"):
    year = input("What year is the car's model? ")
    make = input("What make is the car? ")
    model = input("What model is the car? ")
    doors = input("How many doors does the car have? ")
    roof = input("What type of roof does the car have? ")

    newCar = Automobile("Car", year, make, model, doors, roof)

    print()
    print("Vehicle type: ", newCar.vehicleType)
    print("Year: ", newCar.year)
    print("Make: ", newCar.make)
    print("Model: ", newCar.model)
    print("Number of doors: ", newCar.doors)
    print("Type of roof: ", newCar.roof)
    print()
    car = input("Is your vehicle a car? Type Yes to continue or No to quit:  ")

print("Goodbye!")