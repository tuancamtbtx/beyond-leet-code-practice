class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Helper function for in-order traversal
        def inorder(node):
            if node is None:
                return

            # Visit left subtree
            yield from inorder(node.left)
            # Visit current node
            yield node.val
            # Visit right subtree
            yield from inorder(node.right)

        # Generator for in-order traversal
        gen = inorder(root)

        # Retrieve the k-th smallest element
        for _ in range(k):
            kth_smallest = next(gen)

        return kth_smallest

# Example usage
# Constructing the BST
#       3
#      / \
#     1   4
#      \
#       2
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

solution = Solution()
k = 2
print(solution.kthSmallest(root, k))  # Output: 2