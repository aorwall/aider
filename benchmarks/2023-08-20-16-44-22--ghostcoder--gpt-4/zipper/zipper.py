class Zipper:
    def __init__(self, tree, trail=[]):
        self.tree = tree
        self.trail = trail

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.tree['value']

    def set_value(self, value):
        return Zipper({'value': value, 'left': self.tree['left'], 'right': self.tree['right']}, self.trail)

    def left(self):
        if self.tree['left'] is None:
            return None
        return Zipper(self.tree['left'], [{'node': self.tree, 'dir': 'right'}] + self.trail)

    def set_left(self, tree):
        if not self.trail:
            return None
        parent = self.trail[0]['node']
        parent['left'] = tree
        return Zipper(parent, self.trail[1:])

    def right(self):
        if self.tree['right'] is None:
            return None
        return Zipper(self.tree['right'], [{'node': self.tree, 'dir': 'left'}] + self.trail)

    def set_right(self, tree):
        if not self.trail:
            return None
        parent = self.trail[0]['node']
        parent['right'] = tree
        return Zipper(parent, self.trail[1:])

    def up(self):
        if not self.trail:
            return None
        parent = self.trail[0]['node']
        direction = self.trail[0]['dir']
        parent[direction] = self.tree
        return Zipper(parent, self.trail[1:])

    def to_tree(self):
        if not self.trail:
            return self.tree
        return self.up().to_tree()