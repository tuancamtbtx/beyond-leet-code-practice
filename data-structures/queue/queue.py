class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def peek(self):
        return self.front.value
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, value):
        pass

    def dequeue(self):
        pass
    
    def display(self):
        pass