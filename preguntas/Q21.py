#  Write a Python class to represent a rectangle, including 
# methods to calculate its area and perimeter.

class Rectangle:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def area(self):
        return self.l1 * self.l2
    
    def perimeter(self):
        return self.l1*2 + self.l2*2
    
rectangle = Rectangle(4,6)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")