def check_recursively(node, lower_bound=MIN_INT, upper_bound=MAX_INT):
    if not root:
        return True
    if node.value < lower_bound or node.value > upper_bound:
        return False
    else:
        return (check_recursively(node.left, lower_bound, min(node.value, upper_bound)) and
            check_recursively(node.right, max(lower_bound, node.value), upper_bound))

