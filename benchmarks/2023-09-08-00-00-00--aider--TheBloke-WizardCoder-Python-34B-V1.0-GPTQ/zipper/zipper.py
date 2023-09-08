class Zipper:
    def __init__(self, tree, focus=None, parent=None):
        self.tree = tree
        self.focus = focus
        self.parent = parent

    @staticmethod
    def from_tree(tree):
        return Zipper(tree, focus=tree)

    def value(self):
        if self.focus is None:
            return None
        return self.focus.value

    def set_value(self, value):
        if self.focus is None:
            return self
        self.focus.value = value
        return self

    def left(self):
        if self.focus is None or self.parent is None or self.focus not in self.parent.children:
            return None
        index = self.parent.children.index(self.focus)
        if index == 0:
            return None
        return Zipper(self.tree, focus=self.parent.children[index - 1], parent=self.parent)

    def right(self):
        if self.focus is None or self.parent is None or self.focus not in self.parent.children:
            return None
        index = self.parent.children.index(self.focus)
        if index == len(self.parent.children) - 1:
            return None
        return Zipper(self.tree, focus=self.parent.children[index + 1], parent=self.parent)

    def up(self):
        if self.focus is None or self.parent is None:
            return None
        return Zipper(self.tree, focus=self.parent, parent=self.parent.parent)

    def to_tree(self):
        return self.tree
