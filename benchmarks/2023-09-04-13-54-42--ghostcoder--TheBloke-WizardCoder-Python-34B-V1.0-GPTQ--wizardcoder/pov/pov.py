import unittest
from tree import Tree, Node

class TestPOV(unittest.TestCase):
    def test_find_node_index(self):
        nodes = [Node('a'), Node('b'), Node('c')]
        self.assertEqual(0, find_node_index(nodes, 'a'))
        self.assertEqual(1, find_node_index(nodes, 'b'))
        self.assertEqual(2, find_node_index(nodes, 'c'))

        with self.assertRaises(NodeNotFoundException):
            find_node_index(nodes, 'd')

    def test_find_new_root(self):
        tree = Tree('a', [Node('b', [Node('c'), Node('d')]), Node('e', [Node('f')])])

        new_tree = find_new_root(tree, 'a', 'b')
        self.assertEqual(['b', ['c', 'd']], [new_tree.label, [child.label for child in new_tree.children]])

        new_tree = find_new_root(tree, 'a', 'e')
        self.assertEqual(['e', ['f']], [new_tree.label, [child.label for child in new_tree.children]])

        with self.assertRaises(NodeNotFoundException):
            find_new_root(tree, 'a', 'g')

    def test_find_path(self):
        tree = Tree('a', [Node('b', [Node('c'), Node('d')]), Node('e', [Node('f')])])

        path = find_path(tree.root, 'a', 'c')
        self.assertEqual(['a', 'b', 'c'], [node.label for node in path])

        path = find_path(tree.root, 'a', 'f')
        self.assertEqual(['a', 'e', 'f'], [node.label for node in path])

        with self.assertRaises(NotAPathException):
            find_path(tree.root, 'a', 'z')

    def test_tree_from_pov(self):
        tree = Tree('a', [Node('b', [Node('c'), Node('d')]), Node('e', [Node('f')])])

        subtree = tree.from_pov('b')
        self.assertEqual({'b': ['c', 'd']}, {subtree.label: [child.label for child in subtree.children]})

        subtree = tree.from_pov('c')
        self.assertEqual({'c': [], 'd': []}, {node.label: [child.label for child in node.children] for node in subtree.children})

        with self.assertRaises(ValueError):
            tree.from_pov('z')

    def test_tree_path_to(self):
        tree = Tree('a', [Node('b', [Node('c'), Node('d')]), Node('e', [Node('f')])])

        path = tree.path_to('a', 'c')
        self.assertEqual(['a', 'b', 'c'], path)

        path = tree.path_to('a', 'f')
        self.assertEqual(['a', 'e', 'f'], path)

        with self.assertRaises(ValueError):
            tree.path_to('a', 'z')

if __name__ == "__main__":
    unittest.main()