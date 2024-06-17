from node import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def display(self):
        current = self.head
        while current:
            print(f"{current.value} ", end="")
            current = current.next
            if(current is not None):
                print("-> ", end="")
        print()


    def add_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def add_head(self, node):
        node.next = None
        if self.head is None:
            self.head = node
            self.tail = node
            return
        print(f"Adding {node.value} to the head")
        print(f"Current head is {self.head.value}")
        node.next = self.head
        self.head = node

    def insert_node(self, index, node):
        if self.head is None:
            self.head = node
            self.tail = node
        
        current_node = self.head
        pos = 0
        while current_node is not None and pos < index - 1:
            current_node = current_node.next
            pos += 1
        print(f"Current Node {current_node.value} at index {pos}")
        if current_node is None:
            return
        # set next cua node bang current_node.next
        node.next = current_node.next
        current_node.next = node
    def delete_node(self, index):
        if self.head is None:
            return
        current_node = self.head
        pos = 0
        # duyet toi vi tri index - 1
        while current_node is not None and pos < index - 1:
            current_node = current_node.next
            pos += 1
        if current_node is None or current_node.next is None:
            return
        current_node.next = current_node.next.next

    def find_node(self, value):
        if self.head is None:
            return False
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


def main():
    linked_list = LinkedList()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    linked_list.add_tail(node_1)
    linked_list.add_tail(node_2)
    linked_list.add_tail(node_3)
    linked_list.add_tail(node_4)
    linked_list.add_tail(node_6)
    linked_list.add_head(node_5)
    print("Linked list:")
    linked_list.display()
    linked_list.delete_node(2)
    print("Linked list after remove")
    linked_list.display()

    print("Insert Node at index 2")
    linked_list.insert_node(2, node_7)
    linked_list.insert_node(3, node_8)

    linked_list.display()
    is_exist = linked_list.find_node(10)
    print("Find node whose value is 10: ", is_exist)
if __name__ == "__main__":
    main()