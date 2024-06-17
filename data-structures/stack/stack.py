class Node:
    def __init__(self,value, next = None) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    # Method to add data to the stack
    # adds to the start of the stack
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    # Remove element that is the current head (start of the stack)
    def pop(self):
        if self.head is None:
            return None
        else:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            return pop_node.value
    # Returns the head node data
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.value

    def display(self):
        current_node = self.head
        if self.is_empty():
            print("Stack is empty")
            return
        while current_node:
            print(current_node.value, end = " ")
            current_node = current_node.next

    def is_empty(self):
        if self.head is None:
            return True
        return False


def main():
    stack = Stack()
    node_1 = 1
    node_2 = 2
    node_3 = 3
    node_4 = 4
    node_5 = 5
    node_6 = 6
    node_7 = 7
    node_8 = 8
    stack.push(node_1)
    stack.push(node_2)
    stack.push(node_3)
    stack.push(node_4)
    stack.push(node_5)
    stack.push(node_6)
    stack.pop()
    print("stack:")
    stack.display()

if __name__ == "__main__":
    main()