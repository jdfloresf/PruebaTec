# 25. Write a Python class to represent a car, including attributes 
# for make, model, and year, and a method to display car details.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year

    def dispaly_info(self):
        print("Car Information")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


car = Car("VW", "Jetta", 2018)
car.dispaly_info()
