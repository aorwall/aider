class Zipper:
    def __init__(self, tree, path=None):
        self._tree = tree
        if path is None:
            self._path = []
        else:
            self._path = path
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self._node().val

    def set_value(self, val):
        self._node().val = val
        return self

    def left(self):
        child_index = self._child_index()
        if child_index is None or child_index == 0:
            raise ValueError("Cannot move left")
        return Zipper(self._tree, self._path[:-1] + [child_index - 1])

    def right(self):
        child_index = self._child_index()
        if child_index is None or child_index >= len(self._parent().children) - 1:
            raise ValueError("Already at the rightmost child")
        return Zipper(self._tree, self._path[:-1] + [child_index + 1])

    def up(self):
        if not self._path:
            raise ValueError("Already at root node")
        return Zipper(self._tree, self._path[:-2])

    def to_tree(self):
        return self._tree

    def _node(self):
        curr = self._tree
        for i in self._path:
            curr = curr.children[i]
        return curr

    def _parent(self):
        if not self._path:
            return None
        curr = self._tree
        for i in self._path[:-1]:
            curr = curr.children[i]
        return curr

    def _child_index(self):
        if not self._path:
            return None
        return self._path[-1]
