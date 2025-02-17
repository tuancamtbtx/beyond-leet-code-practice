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

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)
        
    def display(self):
        """Display all items in the queue."""
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("None")

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeued:", queue.dequeue())  # Output: 1
print("Front item:", queue.peek())   # Output: 2
print("Queue size:", queue.size())   # Output: 2
print("Is queue empty?", queue.is_empty())  # Output: False

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        new_node = Node(item)
        if self.rear is None:
            # If the queue is empty, both front and rear will point to the new node
            self.front = self.rear = new_node
        else:
            # Add the new node at the end of the queue and change rear
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            return None
        # Retrieve the front item and move the front pointer to the next node
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            # If the queue becomes empty, set rear to None as well
            self.rear = None
        self._size -= 1
        return dequeued_value

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if self.is_empty():
            return None
        return self.front.value

    def size(self):
        """Return the number of items in the queue."""
        return self._size

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeued:", queue.dequeue())  # Output: 1
print("Front item:", queue.peek())   # Output: 2
print("Queue size:", queue.size())   # Output: 2
print("Is queue empty?", queue.is_empty())  # Output: False