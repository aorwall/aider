def tree_from_traversals(preorder, inorder):
  """
  Reconstructs a binary tree from its pre-order and in-order traversals.

  Args:
    preorder: A list of the values in the tree in pre-order.
    inorder: A list of the values in the tree in in-order.

  Returns:
    A binary tree.

  Raises:
    ValueError: If the traversals are not the same length, do not share the same
      elements, or contain duplicate elements.
  """

  # Check that the traversals are the same length.
  if len(preorder) != len(inorder):
    raise ValueError("traversals must have the same length")

  # Check that the traversals share the same elements.
  if set(preorder) != set(inorder):
    raise ValueError("traversals must have the same elements")

  # Check that the elements are unique.
  if len(preorder) != len(set(preorder)):
    raise ValueError("traversals must contain unique items")

  # Create an empty tree.
  tree = {}

  # Recursively build the tree from the traversals.
  _build_tree(tree, preorder, inorder, 0, len(preorder) - 1)

  # Return the tree.
  return tree

def _build_tree(tree, preorder, inorder, start, end):
  """
  Recursively builds a binary tree from its pre-order and in-order traversals.

  Args:
    tree: A dictionary representing the tree.
    preorder: A list of the values in the tree in pre-order.
    inorder: A list of the values in the tree in in-order.
    start: The start index of the traversals.
    end: The end index of the traversals.

  Raises:
    ValueError: If the traversals are not the same length, do not share the same
      elements, or contain duplicate