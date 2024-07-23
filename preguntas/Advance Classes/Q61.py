# 61. Write a Python class to implement a basic stack data structure

class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack)
print("Top item:", stack.peek())
print("Stack size:", stack.size())
print("Pop item:", stack.pop())
print("Stack after pop:", stack)
print("Is stack empty?", stack.is_empty())
