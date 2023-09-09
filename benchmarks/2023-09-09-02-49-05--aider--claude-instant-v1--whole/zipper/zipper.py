from typing import Optional

class Node:
    def __init__(self, value, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.value = value
        self.left = left 
        self.right = right

class Zipper:
    def __init__(self, tree: Node, focus: Node):
        self.tree = tree
        self.focus = focus

    @staticmethod
    def from_tree(tree: Node) -> 'Zipper':
        return Zipper(tree, tree)

    def value(self) -> any:
        return self.focus.value

    def set_value(self, value: any) -> 'Zipper':
        self.focus.value = value
        return self

    def left(self) -> 'Zipper':
        if self.focus.left:
            return Zipper(self.tree, self.focus.left)
        else:
            return self

    def right(self) -> 'Zipper':
        if self.focus.right:
            return Zipper(self.tree, self.focus.right)
        else:
            return self

    def up(self) -> 'Zipper':
        if self.focus.parent:
            return Zipper(self.tree, self.focus.parent)
        else:
            return self

    def to_tree(self) -> Node:
        return self.tree
