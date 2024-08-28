# Linked List

A Linked List is a fundamental data structure used in computer science to store a collection of elements. Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, each element, known as a node, contains a value and a reference (or link) to the next node in the sequence. This structure allows for efficient insertion and deletion of elements, making it a versatile tool for many applications.

### Types of Linked Lists

1. **Singly Linked List**: Each node points to the next node in the sequence.
2. **Doubly Linked List**: Each node points to both the next and the previous nodes, allowing for traversal in both directions.
3. **Circular Linked List**: The last node points back to the first node, forming a circle.

### Basic Operations

1. **Insertion**: Adding a new node to the list.
2. **Deletion**: Removing a node from the list.
3. **Traversal**: Accessing each node in the list to perform some operation.
4. **Search**: Finding a node with a specific value.

### Example of a Singly Linked List in Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = SinglyLinkedList()
linked_list.insert_at_beginning(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.display()  # Output: 1 -> 2 -> 3 -> None
print(linked_list.search(2))  # Output: True
linked_list.delete_node(2)
linked_list.display()  # Output: 1 -> 3 -> None
print(linked_list.search(2))  # Output: False
```

### Advantages of Linked Lists

1. **Dynamic Size**: Linked lists can grow and shrink in size dynamically.
2. **Efficient Insertions/Deletions**: Inserting or deleting nodes does not require shifting elements, as in arrays.

### Disadvantages of Linked Lists

1. **Memory Overhead**: Each node requires extra memory for storing the reference to the next node.
2. **Sequential Access**: Accessing elements by index is slower compared to arrays since it requires traversal from the head.

Linked lists are a powerful tool for managing collections of data, especially when frequent insertions and deletions are required. Understanding how to implement and use linked lists is essential for any computer science student or software developer.