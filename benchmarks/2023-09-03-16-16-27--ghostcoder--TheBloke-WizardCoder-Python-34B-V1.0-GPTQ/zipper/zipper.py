class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

    def __repr__(self):
        return f"Node({self.val}, {self.children})"


class Zipper:
    def __init__(self, tree, path=()):
        self._root = tree
        self._focus = tree
        self._path = path


    @property
    def value(self):
        return self._focus.val


    def prev(self):
        idx = self._path[-1] - 1 if len(self._path) > 0 else 0
        parent = self._focus if len(self._path) == 0 else self._at_index(self._path[:-1])
        if idx < len(parent.children):
            self._focus = parent.children[idx]
            self._path += (idx,)
        return self


    def next(self):
        idx = self._path[-1] + 1 if len(self._path) > 0 else 0
        parent = self._focus if len(self._path) == 0 else self._at_index(self._path[:-1])
        if idx < len(parent.children):
            self._focus = parent.children[idx]
            self._path += (idx,)
        return self


    def up(self):
        if len(self._path) <= 1:
            self._focus = self._root
            self._path = ()
        else:
            self._focus = self._at_index(self._path[:-2])
            self._path = self._path[:-2]
        return self


    def insert_before(self, val):
        parent = self._at_index(self._path[:-1])
        index = self._path[-1]
        parent.children.insert(index, Node(val))
        self._focus = parent.children[index]
        self._path += (index,)
        return self

    def insert_after(self, val):
        parent = self._at_index(self._path[:-1])
        index = self._path[-1] + 1
        parent.children.insert(index, Node(val))
        self._focus = parent.children[index]
        self._path += (index,)
        return self

    def delete(self):
        parent = self._at_index(self._path[:-1])
        index = self._path[-1]
        del parent.children[index]
        if index >= len(parent.children):
            self._focus = parent
            self._path = self._path[:-1] + (len(parent.children),)
        elif index == 0:
            self._focus = parent.children[0]
            self._path = self._path[:-1] + (0,)
        else:
            self._focus = parent.children[index - 1]
            self._path = self._path[:-1] + (index - 1,)
        return self


    def _at_index(self, path):
        node = self._root
        for i in path:
            node = node.children[i]
        return node


    def set_value(self, val):
        self._focus.val = val
        return self

    def to_tree(self):
        return self._root


    @classmethod
    def from_tree(cls, tree):
        return cls(tree)
