class TreeNode:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []


def btree_min_depth(n: TreeNode):
    """
    Finds the minimal depth of a binary tree through depth first search.

    :param n: root node
    :return: Minimum depth of binary tree.
    """
    assert len(n.children) <= 2
    if not n: return 0
    nr_children = len(n.children)
    if nr_children in {0, 1}:
        return 1
    else:
        return min(btree_min_depth(n.children[0]), btree_min_depth(n.children[1])) + 1
