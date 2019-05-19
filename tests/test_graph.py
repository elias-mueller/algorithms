from algorithms.graphs.data_structures import *


def test_min_height_binary_tree():
    root = TreeNode()
    assert tree_min_height(root) == 1

    root.children.append(TreeNode(root))
    root.children.append(TreeNode(root))
    assert tree_min_height(root) == 2

    root.children[0].children.append(TreeNode(root))
    assert tree_min_height(root) == 2
