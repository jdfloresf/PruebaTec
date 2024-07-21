# 23. Write a Python class to represent a student, including attributes 
# for name, age, and grade, and methods to display the student details.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade

    def dispaly_info(self):
        print("Student Information")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


std = Student("Juan", 20, 4)
std.dispaly_info()