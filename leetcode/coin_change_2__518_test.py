import unittest

from coin_change_2__518 import change 


class ChangeTest(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(1, change(1, [1]))

    def test_online_judge_cases(self):
        amount = 5
        coins = [1, 2, 5]
        self.assertEqual(4, change(amount, coins))

        amount = 3
        coins = [2]
        self.assertEqual(0, change(amount, coins))

        amount = 10
        coins = [10]
        self.assertEqual(1, change(amount, coins))


if __name__ == "__main__":
    unittest.main()
