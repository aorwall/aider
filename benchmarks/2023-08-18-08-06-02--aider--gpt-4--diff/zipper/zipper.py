class Zipper:
    def __init__(self, tree, path=[]):
        self.tree = tree
        self.path = path

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def to_tree(self):
        return self.tree if not self.path else self.up().to_tree()

    def value(self):
        return self.tree['value']

    def set_value(self, value):
        return Zipper({'value': value, 'left': self.tree['left'], 'right': self.tree['right']}, self.path)

    def left(self):
        return None if not self.tree['left'] else Zipper(self.tree['left'], [{'dir': 'left', 'tree': self.tree}] + self.path)

    def set_left(self, tree):
        return Zipper({'value': self.tree['value'], 'left': tree, 'right': self.tree['right']}, self.path)

    def right(self):
        return None if not self.tree['right'] else Zipper(self.tree['right'], [{'dir': 'right', 'tree': self.tree}] + self.path)

    def set_right(self, tree):
        return Zipper({'value': self.tree['value'], 'left': self.tree['left'], 'right': tree}, self.path)

    def up(self):
        if not self.path:
            return None
        dir, tree = self.path[0]['dir'], self.path[0]['tree']
        new_tree = {'value': tree['value'], 'left': self.tree if dir == 'left' else tree['left'], 'right': self.tree if dir == 'right' else tree['right']}
        return Zipper(new_tree, self.path[1:])
