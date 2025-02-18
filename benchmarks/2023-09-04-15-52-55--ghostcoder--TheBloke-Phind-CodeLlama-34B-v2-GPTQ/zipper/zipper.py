class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Zipper:
    def __init__(self, tree):
        self._focus = None
        self._stack = []
        self._root = Node(*tree)

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self._focus.value

    def set_value(self, value):
        self._focus.value = value
        return self

    def left(self):
        if not self._focus or not self._focus.left:
            raise Exception('No left child')
        self._stack.append((self._focus, 'left'))
        self._focus = self._focus.left
        return self

    def set_left(self, left):
        if not self._focus:
            self._focus = Node(None, left=left)
        else:
            self._focus.left = left
        return self

    def right(self):
        if not self._focus or not self._focus.right:
            raise Exception('No right child')
        self._stack.append((self._focus, 'right'))
        self._focus = self._focus.right
        return self

    def set_right(self, right):
        if not self._focus:
            self._focus = Node(None, right=right)
        else:
            self._focus.right = right
        return self

    def up(self):
        try:
            prev_node, direction = self._stack.pop()
            if direction == 'left':
                prev_node.left = self._focus
            else:
                prev_node.right = self._focus
            self._focus = prev_node
        except IndexError:
            # We have reached the root
            pass
        return self

    def to_tree(self):
        while len(self._stack) > 0:
            self.up()
        return self._root
