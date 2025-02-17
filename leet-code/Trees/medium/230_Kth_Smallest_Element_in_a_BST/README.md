To find the k-th smallest element in a Binary Search Tree (BST), we can leverage the properties of the BST and perform an in-order traversal. An in-order traversal of a BST visits the nodes in ascending order, which makes it ideal for finding the k-th smallest element.

Here's a step-by-step approach to solve this problem:

1. **In-order Traversal:** Perform an in-order traversal of the BST. As you traverse the tree, keep a counter to track the number of nodes visited.

2. **Track the k-th Node:** When the counter reaches `k`, the current node is the k-th smallest element.

3. **Optimization:** If you find the k-th smallest element, you can stop the traversal early to avoid unnecessary work.

Here is the Python implementation:

```python
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
```

### Explanation:

- **TreeNode Class:** Represents a node in the BST with a value (`val`) and pointers to left and right children.

- **Solution Class:** Contains the `kthSmallest` method to find the k-th smallest element:
  - **inorder Function:** A generator function that performs an in-order traversal of the BST. It yields node values one by one, in ascending order.
  - **Generator Usage:** We create a generator `gen` from the `inorder` function and use `next(gen)` `k` times to get the k-th smallest element.

- **Example Usage:** Constructs a simple BST and finds the 2nd smallest element, which is `2` in this case.

This approach efficiently finds the k-th smallest element with a time complexity of O(H + k), where H is the height of the tree. The space complexity is O(H) due to the recursion stack during the traversal.