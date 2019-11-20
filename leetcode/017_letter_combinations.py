import itertools
from typing import List
import unittest

NS_TO_LS = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

class Solution:
    def letterCombinationsDepthFirst(self, digits: str) -> List[str]:
        combos: List[str] = []
        if len(digits) == 0: return combos

        def lcr(i: int, acc: List[str]):
            if i >= len(digits): return combos.append("".join(acc))
            for l in NS_TO_LS[digits[i]]: 
                acc.append(l)
                lcr(i+1, acc)
                acc.pop()

        lcr(0, [])
        return combos

    def letterCombinationsPythonic(self, digits: str) -> List[str]:
        if not digits: return []
        chars = []
        for d in digits:
            chars.append(NS_TO_LS[d])
        return ["".join(c) for c in itertools.product(*chars)]


    def letterCombinations(self, digits: str) -> List[str]:
        N = 1
        for d in digits: N *= len(NS_TO_LS[d])
        combos = [None] * N

        for i in range(N):
            combo, t = [], i
            for (j, d) in enumerate(digits):
                letters = NS_TO_LS[d]
                combo.append(letters[t % len(letters)])
                t /= len(letters)
            combos[i] = "".join(combo)
        return combos



class SolutionTest(unittest.TestCase):

    def test_all_digits_numbers(self):
        self.assertEqual(["a", "b", "c"], Solution().letterCombinations("2"))
        self.assertEqual(["a", "b", "c"], Solution().letterCombinationsPythonic("2"))
        self.assertEqual(["a", "b", "c"], Solution().letterCombinationsDepthFirst("2"))

if __name__ == "__main__": unittest.main()
