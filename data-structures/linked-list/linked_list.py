from node import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        return
    
    def display(self):
        current = self.head
        while current:
            print(f"{current.value} ", end="")
            current = current.next
            if(current is not None):
                print("-> ", end="")
        print()

def main():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(4)

    linked_list.display()

if __name__ == "__main__":
    main()