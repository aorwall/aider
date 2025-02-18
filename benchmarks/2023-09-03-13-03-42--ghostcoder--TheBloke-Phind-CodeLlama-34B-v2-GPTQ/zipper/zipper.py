class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.left_sibling = None
        self.right_sibling = None
class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.left_sibling = None
        self.right_sibling = None
class Zipper:
    def __init__(self, tree=None):
        self._root = tree
        self._focus = tree

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self._focus.value if self._focus else None

    def set_value(self, value):
        if self._focus:
            self._focus.value = value
        return self

    def left(self):
        if self._focus and self._focus.left:
            self._focus = self._focus.left
        return self

    def set_left(self, tree):
        if self._focus:
            self._focus.left = tree
        return self

    def right(self):
        if self._focus and self._focus.right:
            self._focus = self._focus.right
        return self

    def set_right(self, tree):
        if self._focus:
            self._focus.right = tree
        return self

    def up(self):
        if self._focus and self._focus.parent:
            self._focus = self._focus.parent
        return self

    def to_tree(self):
        return self._root
