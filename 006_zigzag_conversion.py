import unittest

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows <= 1: return s

        converted, current_row = [], 0
        while current_row < num_rows:
            i, c, js = current_row, 0, []
            if current_row < num_rows-1: js.append(((num_rows-1)-current_row) * 2)
            if current_row > 0: js.append(current_row * 2)
            while i < len(s):
                converted.append(s[i])
                jb = js[c % len(js)]
                i, c = i+jb, c+1
            current_row += 1
        return "".join(converted)

class SolutionTest(unittest.TestCase):

    def test_convert(self):
        self.assertEqual("AEBDFC", Solution().convert("ABCDEF", 3))
        self.assertEqual("PAHNAPLSIIGYIR", Solution().convert("PAYPALISHIRING", 3))
        self.assertEqual("PINALSIGYAHRPI", Solution().convert("PAYPALISHIRING", 4))

if __name__ == "__main__":
    unittest.main()
