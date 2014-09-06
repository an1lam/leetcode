def largest(root_node):
    if root_node.right_child is not None:
        return largest(root_node.right_child)
    return root_node

def second_largest(root_node):
    largest_node = largest(root_node)
    if largest_node.left_child is not None:
        second_largest = largest(largest_node.left_child)
    else:
        second_largest = largest_node.parent
    return second_largest.value
