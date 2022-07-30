class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if self.value == value:
            return
        elif value < self.value:
            if self.left is None: # at end leaf node 
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        print(self.value)

def main():
    root = Node(12)
    root.insert(1)
    root.insert(2)
    root.insert(20)
    root.insert(100)
    root.print_tree()

if __name__ == "__main__":
    main()