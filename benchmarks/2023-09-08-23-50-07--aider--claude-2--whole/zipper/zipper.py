class Zipper:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def from_tree(tree):
        return Zipper(tree["value"], tree["left"], tree["right"])

    def to_tree(self):
        return {
            "value": self.value,
            "left": self.left.to_tree() if self.left else None,
            "right": self.right.to_tree() if self.right else None
        }

    def value(self):
        return self.value

    def set_value(self, new_value):
        return Zipper(new_value, self.left, self.right)

    def left(self):
        return self.left

    def set_left(self, new_left):
        return Zipper(self.value, new_left, self.right)

    def right(self):
        return self.right

    def set_right(self, new_right):
        return Zipper(self.value, self.left, new_right)

    def up(self):
        return None
