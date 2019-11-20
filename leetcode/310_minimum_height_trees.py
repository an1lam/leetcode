from typing import Dict, List, Set
import sys
import unittest


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]

        g = {}
        for i in range(n): 
            g[i] = []
        for e in edges: 
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        cln, oln = [], []
        for sn, al in g.items():
            if len(al) == 1: oln.append(sn)

        tn = n
        while tn > 2:
            for cn in oln:
                if len(g[cn]) > 0:
                    fn = g[cn][0] 
                    g[fn].remove(cn)
                    tn -= 1
                    if len(g[fn]) == 1: cln.append(fn)
            oln = cln
            cln = []
        return oln


        

class SolutionTest(unittest.TestCase):
    def test_find_min_height_trees(self):
        self.assertEqual([1], Solution().findMinHeightTrees(4,  [[1, 0], [1, 2], [1, 3]]))
        self.assertEqual([3, 4], Solution().findMinHeightTrees(6,  [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))


if __name__ == "__main__":
    unittest.main()
