class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Zipper:
    def __init__(self, root=None, parent=None, direction="root"):
        self._focus = TreeNode(root) if root else None
        self._parent = parent
        self._direction = direction

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self._focus.value if self._focus else None

    def set_value(self, new_val):
        self._focus.value = new_val
        return self

    def left(self):
        if self._focus and self._focus.left:
            return Zipper(self._focus.left, self, "left")
        return Zipper()

    def set_left(self, tree):
        self._focus.left = tree
        return self

    def right(self):
        if self._focus and self._focus.right:
            return Zipper(self._focus.right, self, "right")
        return Zipper()

    def set_right(self, tree):
        self._focus.right = tree
        return self

    def up(self):
        if self._parent:
            return Zipper(self._parent._focus, self._parent._parent, self._parent._direction)
        return Zipper()

    def to_tree(self):
        return self._focus if self._focus else None
