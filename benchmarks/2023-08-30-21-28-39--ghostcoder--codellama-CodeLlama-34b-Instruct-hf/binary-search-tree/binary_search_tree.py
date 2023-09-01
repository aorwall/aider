class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        self.size = 0
        self.insert(tree_data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def search(self, data):
        if self.root is None:
            return None
        else:
            return self._search(data, self.root)

    def _search(self, data, node):
        if data == node.data:
            return node
        elif data < node.data:
            if node.left is None:
                return None
            else:
                return self._search(data, node.left)
        else:
            if node.right is None:
                return None
            else:
                return self._search(data, node.right)

    def delete(self, data):
        if self.root is None:
            return None
        else:
            self._delete(data, self.root)

    def _delete(self, data, node):
        if data == node.data:
            if node.left is None and node.right is None:
                self.size -= 1
                return None
            elif node.left is None:
                self.size -= 1
                return node.right
            elif node.right is None:
                self.size -= 1
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.data = min_node.data
                self._delete(min_node.data, node.right)
        elif data < node.data:
            if node.left is None:
                return None
            else:
                self._delete(data, node.left)
        else:
            if node.right is None:
                return None
            else:
                self._delete(data, node.right)

    def _find_min(self, node):
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)

    def _find_max(self, node):
        if node.right is None:
            return node
        else:
            return self._find_max(node.right)