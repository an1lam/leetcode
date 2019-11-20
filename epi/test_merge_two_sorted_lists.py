import unittest

from merge_two_sorted_lists import merge_two_sorted_lls
from merge_two_sorted_lists import Node


class TestMergeTwoSortedLinkedLists(unittest.TestCase):

    def test_both_nonempty_lists(self):
        l1 = Node(val=1, next=Node(val=4))
        l2 = Node(val=2, next=Node(val=3))

        sll = merge_two_sorted_lls(l1, l2)

        for i in range(1, 5):
            self.assertEqual(i, sll.val)
            sll = sll.next

    def test_empty_nonempty_list_pair(self):
        l1 = None
        l2 = Node(val=1, next=Node(val=2))

        sll = merge_two_sorted_lls(l1, l2)

        for i in range(1, 3):
            self.assertEqual(i, sll.val)
            sll = sll.next


if __name__ == "__main__":
    unittest.main()
