class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self._update_height(x)
        self._update_height(y)

        return y

    def _rebalance(self, node):
        # Update the height of the ancestor node
        self._update_height(node)

        # Get the balance factor
        balance = self._balance_factor(node)

        # Left Left Case
        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._rotate_right(node)

        # Left Right Case
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._rotate_left(node)

        # Right Left Case
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, node, key):
        # 1. Perform the normal BST insert
        if not node:
            return TreeNode(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # 2. Update height of this ancestor node
        self._update_height(node)

        # 3. Get the balance factor of this ancestor node to check whether
        #    this node became unbalanced
        return self._rebalance(node)

    def delete(self, node, key):
        # 1. Perform standard BST delete
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        # If the tree had only one node then return
        if node is None:
            return node

        # 2. Update height of the current node
        self._update_height(node)

        # 3. Rebalance the node
        return self._rebalance(node)

    def _min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._min_value_node(node.left)

    def search(self, node, key):
        # Standard BST search
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self.search(node.left, key)

        return self.search(node.right, key)

    def pre_order(self, node):
        if not node:
            return
        print(node.key, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

# Example usage
avl_tree = AVLTree()
root = None

# Insert nodes
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl_tree.insert(root, key)

# Pre-order traversal
print("Pre-order traversal of the constructed AVL tree is:")
avl_tree.pre_order(root)
print()

# Delete a node
root = avl_tree.delete(root, 30)

# Pre-order traversal after deletion
print("Pre-order traversal after deletion of 30:")
avl_tree.pre_order(root)
print()