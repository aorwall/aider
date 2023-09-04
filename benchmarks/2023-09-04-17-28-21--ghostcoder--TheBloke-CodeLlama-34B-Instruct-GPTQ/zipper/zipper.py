class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Zipper:
    def __init__(self, tree, focus):
        self._root = tree
        self._focus = focus

    @staticmethod
    def from_tree(tree):
        return Zipper(tree, tree)

    def value(self):
        return self._focus.value

    def set_value(self, value):
        self._focus.value = value

    def left(self):
        return self._focus.left

    def set_left(self, left):
        self._focus.left = left

    def right(self):
        return self._focus.right

    def set_right(self, right):
        self._focus.right = right

    def up(self):
        current = self._root
        while current.left != self._focus and current.right != self._focus:
            current = current.left if current.left else current.right
        self._focus = current

    def down(self):
        pass

    def to_tree(self):
        return self._root


if __name__ == "__main__":
    # Test case 1
    tree = Node(1, Node(2), Node(3))
    zipper = Zipper.from_tree(tree)
    print(zipper.value())  # Output: 1
    print(zipper.left().value())  # Output: 2
    print(zipper.right().value())  # Output: 3
    zipper.set_value(4)
    zipper.set_left(Node(5))
    zipper.set_right(Node(6))
    print(zipper.to_tree())  # Output: Node(4, Node(5), Node(6))

    # Test case 2
    tree = Node(1, Node(2, Node(4)), Node(3, Node(5)))
    zipper = Zipper.from_tree(tree)
    print(zipper.value())  # Output: 1
    print(zipper.left().value())  # Output: 2
    print(zipper.left().down().value())  # Output: 4
    print(zipper.right().value())  # Output: 3
    print(zipper.right().down().value())  # Output: 5
    zipper.set_value(7)
    zipper.set_left(Node(8, Node(9)))
    zipper.set_right(Node(10, Node(11)))
    print(zipper.to_tree())  # Output: Node(7, Node(8, Node(9)), Node(10, Node(11)))
