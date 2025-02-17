class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_tail(self, node:Node=None):
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        self.tail.next = node
        self.tail = node
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.val,end="")
            current_node = current_node.next
            if(current_node is not None):
                print("-> ", end="")
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pass
    def init_linked_list(self, arr):
        linked_list = LinkedList()
        for i in range(len(arr)):
            node = Node(arr[i], None)
            linked_list.add_tail(node)
        print(linked_list)
        return linked_list

def main():
    head = [1,2,3,-3,4]
    solution = Solution()
    linked = solution.init_linked_list(head)
    linked.display()
if __name__ == "__main__":
    main()