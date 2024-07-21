# 27. Write a Python class to represent a book, including attributes 
# for title, author, and number of pages, and a method to display book details.

class Book:
    def __init__(self, title, author, number_pages):
        self.title = title
        self.author = author 
        self.number_pages = number_pages

    def dispaly_info(self):
        print("Car Information")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.number_pages}")


book = Book("La historia del loco", "John Katzenbach", 448)
book.dispaly_info()
