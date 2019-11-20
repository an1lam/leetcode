import unittest

from stack_with_max import StackWithMax


class TestStackWithMax(unittest.TestCase):
    def test_one_push_one_pop(self):
        stack = StackWithMax()
        stack.push(1)
        self.assertEqual(1, stack.max())
        self.assertEqual(1, stack.pop())

    def test_ascending_pushes(self):
        stack = StackWithMax()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.max())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.max())
        self.assertEqual(1, stack.pop())

    def test_descending_pushes(self):
        stack = StackWithMax()
        stack.push(2)
        stack.push(1)
        self.assertEqual(2, stack.max())
        self.assertEqual(1, stack.pop())
        self.assertEqual(2, stack.max())
        self.assertEqual(2, stack.pop())


if __name__ == "__main__":
    unittest.main()
