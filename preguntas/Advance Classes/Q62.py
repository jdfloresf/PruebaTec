# 62. Write a Python class to implement a basic queue data structure.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue)
print("Front item:", queue.peek())
print("Queue size:", queue.size())
print("Dequeue item:", queue.dequeue())
print("Queue after dequeue:", queue)
print("Is queue empty?", queue.is_empty())
