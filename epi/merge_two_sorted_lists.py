class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_lls(l1, l2):
    p1, p2 = l1, l2
    nh = np = Node()

    while p1 and p2:
        p1_nxt, p2_nxt = p1.next, p2.next
        if p1.val <= p2.val:
            np.next = p1
            p1.next = None
            p1 = p1_nxt
        else:
            np.next = p2
            p2.next = None
            p2 = p2_nxt
        np = np.next

    np.next = p1 or p2
    return nh.next
