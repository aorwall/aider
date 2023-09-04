class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Zipper:
    def __init__(self, tree, path):
        self._tree = tree
        self._path = path

    @property
    def value(self):
        return self._current_node().value

    def set_value(self, value):
        current_node = self._current_node()
        new_node = TreeNode(value, current_node.left, current_node.right)
        self._update_parent(new_node)
        return Zipper(self._tree, self._path[:-1])

    def left(self):
        if not self._current_node().left:
            raise ValueError('Cannot move left')
        return Zipper(self._tree, self._path + [0])

    def set_left(self, left):
        current_node = self._current_node()
        new_node = TreeNode(current_node.value, left, current_node.right)
        self._update_parent(new_node)
        return Zipper(self._tree, self._path)

    def right(self):
        if not self._current_node().right:
            raise ValueError('Cannot move right')
        return Zipper(self._tree, self._path + [1])

    def set_right(self, right):
        current_node = self._current_node()
        new_node = TreeNode(current_node.value, current_node.left, right)
        self._update_parent(new_node)
        return Zipper(self._tree, self._path)

    def up(self):
        if len(self._path) < 2:
            raise ValueError('Cannot move up')
        return Zipper(self._tree, self._path[:-2])

    def to_tree(self):
        return self._tree

    def _current_node(self):
        node = self._tree
        for index in self._path:
            node = node.left if index == 0 else node.right
        return node

    def _update_parent(self, new_child):
        if not self._path:
            self._tree = new_child
        else:
            parent = self._current_node().__getattribute__(['left', 'right'][self._path[-1]])
            parent.__setattr__(['left', 'right'][self._path[-2]], new_child)

    @staticmethod
    def from_tree(tree):
        return Zipper(tree, [])

    # These methods were added to fix the errors in the tests
    def get_left(self):
        try:
            return self.left()
        except ValueError:
            return None

    def get_right(self):
        try:
            return self.right()
        except ValueError:
            return None

    def replace_with(self, replacement):
        parent = self.up()
        if self.is_left():
            parent.set_left(replacement)
        elif self.is_right():
            parent.set_right(replacement)
        else:
            raise ValueError("Invalid position")
        return parent

    def is_left(self):
        return self._path and self._path[-1] == 0

    def is_right(self):
        return self._path and self._path[-1] == 1

    def delete(self):
        if not self._path:
            raise ValueError("Cannot delete root of a tree")

        parent = self.up()
        if self.is_left():
            parent.set_left(None)
        elif self.is_right():
            parent.set_right(None)
        else:
            raise ValueError("Invalid position")
        return parent
