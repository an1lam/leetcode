"""
Flipping a tree is itself a trivial operation; just swap left and right.

Therefore, the challenge in this problem is efficiently testing all possible flips. The
naive way to solve this is just to do a tree traversal and for each node, test whether
the tree is equal before and after swapping its left and right children. Since the tree
is limited to 100 nodes, the runtime is something like O(100n). 

Depending on how we traverse the two trees, we can save a bunch of work. Specifically if
we go bottoms-up in the right manner we only have to check whether the current two nodes
are equal are flipped between the two trees.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def count_null_children(node: TreeNode):
    return (node.left is None) + (node.right is None)


def flip_equiv(root1: TreeNode, root2: TreeNode) -> bool:
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    vals_equal = root1.val == root2.val
    unflipped_equal = flip_equiv(root1.left, root2.left) and flip_equiv(
        root1.right, root2.right
    )
    flipped_equal = flip_equiv(root1.left, root2.right) and flip_equiv(
        root1.right, root2.left
    )
    return vals_equal and (unflipped_equal or flipped_equal)
