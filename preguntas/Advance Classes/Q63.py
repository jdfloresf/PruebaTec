# 63. Write a Python class to represent a binary tree with methods for 
# insertion, deletion, and traversal.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, values):
        if node is not None:
            self._inorder_traversal(node.left, values)
            values.append(node.val)
            self._inorder_traversal(node.right, values)
        return values

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, node, values):
        if node is not None:
            values.append(node.val)
            self._preorder_traversal(node.left, values)
            self._preorder_traversal(node.right, values)
        return values

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, node, values):
        if node is not None:
            self._postorder_traversal(node.left, values)
            self._postorder_traversal(node.right, values)
            values.append(node.val)
        return values


tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
print("Inorder traversal:", tree.inorder_traversal())
print("Preorder traversal:", tree.preorder_traversal())
print("Postorder traversal:", tree.postorder_traversal())
tree.delete(20)
print("Inorder traversal after deleting 20:", tree.inorder_traversal())
tree.delete(30)
print("Inorder traversal after deleting 30:", tree.inorder_traversal())
tree.delete(50)
print("Inorder traversal after deleting 50:", tree.inorder_traversal())