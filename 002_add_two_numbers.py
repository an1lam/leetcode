import unittest

class ListNode:
    def __init__(self, x):
        self.val, self.next = x, None

    def __eq__(self, other):
        if type(self) is not type(other): return False
        return self.val == other.val and self.next == other.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = False
        head = pn = ListNode(None)
        while l1 or l2:
            n1, n2 = (l1.val if l1 else 0), (l2.val if l2 else 0)
            s = (n1 + n2 + carry)
            nn = ListNode(s % 10)
            carry = (s >= 10)

            pn.next = nn
            pn = nn
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry: pn.next = ListNode(1)
        return head.next


class SolutionTest(unittest.TestCase):
    def test_basic_add(self):
        l1, l2 = ListNode(1), ListNode(2)
        l1.next, l2.next = ListNode(2), ListNode(3)
        expected = ListNode(3)
        expected.next = ListNode(5)
        self.assertEqual(expected, Solution().addTwoNumbers(l1, l2))

    def test_add_with_carry(self):
        l1, l2 = ListNode(2), ListNode(9)
        l1.next, l2.next = ListNode(2), ListNode(8)
        expected = ListNode(1)
        expected.next = ListNode(1)
        expected.next.next = ListNode(1)
        self.assertEqual(expected, Solution().addTwoNumbers(l1, l2))


if __name__ == "__main__":
    unittest.main()
