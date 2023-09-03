class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for num in tree_data:
            self.add(num)


    def add(self, data):
        """Adds a new element to the BST"""
        if not self.root:
            self.root = TreeNode(data)
        else:
            curr = self.root
            while True:
                if data <= curr.data: # changed from '<' to '<=' and '>' to '<='
                    if not curr.left:
                        curr.left = TreeNode(data)
                        break
                    else:
                        curr = curr.left
                else:
                    if not curr.right:
                        curr.right = TreeNode(data)
                        break
                    else:
                        curr = curr.right

    def _sorted_data(self, node, result):
        """Helper method to get the sorted data recursively"""
        if node:
            self._sorted_data(node.left, result)
            result.append(node.data)
            self._sorted_data(node.right, result)

    @property
    def data(self):
        """Returns the root node of the BST"""
        return self.root

    def sorted_data(self):
        """Returns the sorted list of data in the BST"""
        result = []
        self._sorted_data(self.root, result)
        return result
