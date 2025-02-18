import random
from typing import List

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data: List[int]):
        self.root = None
        for data in tree_data:
            self.insert(data)

    def insert(self, data: int):
        if not self.root:
            self.root = TreeNode(data)
        else:
            curr_node = self.root
            while True:
                if data < curr_node.data:
                    if not curr_node.left:
                        curr_node.left = TreeNode(data)
                        break
                    else:
                        curr_node = curr_node.left
                elif data > curr_node.data:
                    if not curr_node.right:
                        curr_node.right = TreeNode(data)
                        break
                    else:
                        curr_node = curr_node.right

    def data(self):
        return [node.data for node in self._inorder()]

    def _inorder(self):
        stack = []
        curr_node = self.root
        while stack or curr_node:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                yield curr_node
                curr_node = curr_node.right

    def sorted_data(self):
        return list(sorted([node.data for node in self._inorder()]))

if __name__ == "__main__":
    test_cases = 100
    max_elements = 50

    for i in range(test_cases):
        input_list = random.sample(range(-max_elements * 2, max_elements * 2), max_elements)

        bst = BinarySearchTree(input_list)
        assert bst.sorted_data() == sorted(input_list)
