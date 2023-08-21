class Zipper:
    def __init__(self, tree=None, path=[]):
        self.tree = tree
        self.path = path

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def to_tree(self):
        return self.tree

    def value(self):
        return self.tree['value']

    def set_value(self, value):
        self.tree['value'] = value
        return self

    def left(self):
        return Zipper(self.tree['left'], self.path + ['left']) if self.tree['left'] else None

    def set_left(self, tree):
        self.tree['left'] = tree
        return self

    def right(self):
        return Zipper(self.tree['right'], self.path + ['right']) if self.tree['right'] else None

    def set_right(self, tree):
        self.tree['right'] = tree
        return self

    def up(self):
        if not self.path:
            return None
        direction = self.path[-1]
        parent_path = self.path[:-1]
        parent = self.from_tree(self.tree)
        for step in parent_path:
            parent = parent.left() if step == 'left' else parent.right()
        return parent

    def prev(self):
        pass  # Not applicable for binary trees

    def next(self):
        pass  # Not applicable for binary trees

    def insert_before(self, tree):
        pass  # Not applicable for binary trees

    def insert_after(self, tree):
        pass  # Not applicable for binary trees

    def delete(self):
        direction = self.path[-1]
        parent_path = self.path[:-1]
        parent = self.from_tree(self.tree)
        for step in parent_path:
            parent = parent.left() if step == 'left' else parent.right()
        if parent:
            if direction == 'left':
                parent.set_left(None)
            else:
                parent.set_right(None)
        else:
            self.tree = None
        return self
