class Zipper:
    def __init__(self, tree, parent=None, prev=None, next=None):
        self.tree = tree
        self.parent = parent
        self.prev = prev
        self.next = next

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def to_tree(self):
        return self.tree

    def value(self):
        return self.tree[0]

    def set_value(self, value):
        self.tree[0] = value

    def left(self):
        if len(self.tree) > 1:
            return Zipper(self.tree[1], self, None, self.tree[2:])
        else:
            return None

    def set_left(self, left):
        if left is None:
            self.tree = [self.tree[0]]
        else:
            self.tree = [self.tree[0], left.tree] + self.tree[2:]

    def right(self):
        if len(self.tree) > 2:
            return Zipper(self.tree[2], self, self.tree[1], self.tree[3:])
        else:
            return None

    def set_right(self, right):
        if right is None:
            self.tree = [self.tree[0], self.tree[1]]
        else:
            self.tree = [self.tree[0], self.tree[1], right.tree] + self.tree[3:]

    def up(self):
        if self.parent is None:
            return None
        else:
            return Zipper([self.parent.tree[0]] + [self.tree] + self.parent.tree[2:], self.parent.parent, self.parent.prev, self.parent.next)

    def insert_before(self, subtree):
        if self.parent is None:
            return Zipper(subtree, None, None, self.tree)
        else:
            return Zipper(self.parent.tree[0], self.parent.parent, self.parent.prev, [subtree] + [self.tree] + self.parent.tree[2:])

    def insert_after(self, subtree):
        if self.parent is None:
            return Zipper(subtree, None, self.tree, None)
        else:
            return Zipper(self.parent.tree[0], self.parent.parent, [subtree] + [self.tree] + self.parent.tree[2:], self.parent.next)

    def delete(self):
        if self.parent is None:
            return None
        elif self.next is not None:
            return Zipper(self.next.tree, self.parent, self.prev, self.next.next)
        elif self.prev is not None:
            return Zipper(self.prev.tree, self.parent, self.prev.prev, None)
        else:
            return Zipper(self.parent.tree, self.parent.parent, self.parent.prev, self.parent.next)
