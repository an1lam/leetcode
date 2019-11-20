class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        f, p = head, None
        head = head.next

        while f and f.next: 
            s = f.next
            if p: p.next = s
            f.next = s.next
            s.next = f
            p = f
            f = f.next

        return head

