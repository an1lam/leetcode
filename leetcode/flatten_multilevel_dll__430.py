class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head: return None, None
    
    curr = result = head
    prev = None

    while curr is not None:
        if prev is not None:
            curr.prev = prev
        if curr.child is not None:
            tmp = curr.next
            fhead, ftail = flatten(curr.child)
            fhead.prev = curr
            ftail.next = curr.next
            
            curr.child = None
            curr.next = fhead
            
            prev = ftail
            curr = tmp
        else:
            prev = curr
            curr = curr.next
            
    return result, prev
