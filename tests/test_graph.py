from algorithms.graphs.data_structures import *


def test_min_height_binary_tree():
    root = TreeNode()
    assert btree_min_depth(root) == 1

    root.children.append(TreeNode(root))
    root.children.append(TreeNode(root))
    assert btree_min_depth(root) == 2

    root.children[0].children.append(TreeNode(root))
    assert btree_min_depth(root) == 2
