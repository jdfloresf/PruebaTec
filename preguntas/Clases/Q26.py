# 26. Write a Python class to implement a simple calculator with methods 
# for addition, subtraction, multiplication, and division.

class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        print(f"{self.n1} + {self.n2} = {self.n1 + self.n2}")
    
    def sub(self):
        print(f"{self.n1} - {self.n2} = {self.n1 - self.n2}")
    
    def mult(self):
        print(f"{self.n1} * {self.n2} = {self.n1 * self.n2}")
    
    def div(self):
        print(f"{self.n1} / {self.n2} = {self.n1 / self.n2}")

cal = Calculator(8, 2)
cal.add()
cal.sub()
cal.mult()
cal.div()


