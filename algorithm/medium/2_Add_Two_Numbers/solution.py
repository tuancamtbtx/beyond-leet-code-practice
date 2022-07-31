# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    def init_linked_list(self, arr):
        list_node = ListNode(arr[0], None)
        for i in range(len(arr) - 1):
            j = i + 1
            list_node = ListNode(arr[j], list_node)
        return list_node

def main():
    solution = Solution()
    nums1 = [1, 2] # sorted
    list_node = solution.init_linked_list(nums1)
    head = list_node
    while head:
        print(head.val)
        head = head.next
if __name__ == "__main__":
    main()