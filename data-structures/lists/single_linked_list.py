class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.head = None

    def add_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_tail(self, value):
        new_node = Node(value)
        # linked list chua co du lieu chua
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        # duyet toi cuoi de add new node
        while last.next is not None:
            last = last.next
        last.next = new_node
    def display(self):
        head = self.head
        list_values = []
        while(head is not None):
            list_values.append("(" + str(head.value) + ")")
            head = head.next
        print(" -> ".join(list_values))
    def remove_node(self, value):
        pass
    
    def find_x(self, value):
        head = self.head
        list_node = []
        while head is not None:
            if head.value == value:
                list_node.append(head)
            head = head.next
        return list_node
def main():
    s_linked_list = SingleLinkedList()
    s_linked_list.add_head(1)
    s_linked_list.add_tail(221)
    s_linked_list.add_head(2)
    s_linked_list.add_tail(10)
    s_linked_list.add_tail(10)
    s_linked_list.add_tail(10)

    print("Linked list: ")
    s_linked_list.display()
    print("Find value in linked list:")
    finds_10 = s_linked_list.find_x(10)
    for item in finds_10:
        print(item.value)
if __name__ == "__main__":
    main()