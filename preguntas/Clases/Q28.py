# Write a Python class to implement a singly linked list.

class SinglyLinkedList:
    def __init__(self):
        self.lista = []

    def insert(self, data):
        self.lista.append(data)

    def display(self):
        print(self.lista)

lst = SinglyLinkedList()
lst.insert(3)
lst.insert(4)
lst.insert(112)
lst.insert(4141)
lst.display()

