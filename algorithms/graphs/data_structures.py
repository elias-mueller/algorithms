class TreeNode:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []


def tree_min_height(root_node: TreeNode):
    return _tree_min_height(root_node)


def _tree_min_height(n: TreeNode, min_height=0):
    if not n: return min_height
    min_height += 1
    nr_children = len(n.children)
    if nr_children == 0:
        return min_height
    elif nr_children == 1:
        return min_height + 1
    else:
        return min(_tree_min_height(n.children[0], min_height), _tree_min_height(n.children[1], min_height))
