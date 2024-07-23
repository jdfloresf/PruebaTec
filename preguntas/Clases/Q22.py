# 22. Write a Python class to represent a circle, 
# including methods to calculate its area and circumference.
from math import pi

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi*self.r**2
    
    def circumference(self):
        return 2*pi*self.r
    
circle = Circle(4)
print(f"Area: {circle.area()}")
print(f"circumference: {circle.circumference()}")
