import unittest

from alphabet_board_path__1138 import alphabet_board_path


class AlphabetBoardPathTest(unittest.TestCase):
    def test_oj_cases(self):
        self.assertEqual("DDR!UURRR!!DDD!", alphabet_board_path("leet"))
        self.assertEqual("RR!DDRR!UUL!R!", alphabet_board_path("code"))
        self.assertEqual("DDDDD!UUUUURRR!LLLDDDDD!", alphabet_board_path("zdz"))

    def test_edge_cases(self):
        self.assertEqual("!", alphabet_board_path("a"))


if __name__ == "__main__":
    unittest.main()
