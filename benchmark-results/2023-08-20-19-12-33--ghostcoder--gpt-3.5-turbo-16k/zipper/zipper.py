class Zipper:
    def __init__(self, tree, parent=None, left=None, right=None):
        self.tree = tree
        self.parent = parent
        self.left = left
        self.right = right

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.tree[0]

    def set_value(self, value):
        self.tree[0] = value
        return self

    def left(self):
        if self.tree[1]:
            return Zipper(self.tree[1], self.parent, self.left, self.right)
        else:
            return None

    def set_left(self, tree):
        self.tree[1] = tree
        return self

    def right(self):
        if self.tree[2]:
            return Zipper(self.tree[2], self.parent, self.left, self.right)
        else:
            return None

    def set_right(self, tree):
        self.tree[2] = tree
        return self

    def up(self):
        if self.parent:
            return Zipper(self.parent, self.parent[0], self.parent[1], self.parent[2])
        else:
            return None

    def to_tree(self):
        return self.tree