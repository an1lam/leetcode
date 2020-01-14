from collections import deque
from typing import Dict
from typing import List
from typing import Set

"""
Solution, V1: Using graph and BFS.
"""
def build_graph(nums: List[int]):
    graph, roots = {}, set()
    for num in nums:
        graph[num] = set()
        roots.add(num)
        if num-1 in graph:
            roots.remove(num)
            graph[num-1].add(num)
        if num+1 in graph:
            if num+1 in roots: roots.remove(num+1)
            graph[num].add(num+1)
    return graph, roots

def longest_path(graph: Dict[int, List[int]], roots: Set[int]): 

    max_path_len = 0
    visited = set()

    def bfs(source):
        curr_path_len = 0 
        q = deque([source])

        while len(q) > 0:
            curr_path_len += 1
            curr = q.pop()

            if curr not in visited:
                for neighbor in graph[curr]:
                    q.appendleft(neighbor)
                visited.add(curr)
        return curr_path_len


    for node in roots:
        max_path_len = max(bfs(node), max_path_len)
    return max_path_len

def longest_consecutive_sequence__graph(nums: List[int]):
    graph, roots = build_graph(nums)
    return longest_path(graph, roots)

"""
Solution, V2: Basically the same idea but speeding up / simplifying by getting rid of
the need for a graph entirely.
"""

def longest_consecutive_sequence__set(nums: List[int]):
    s, ml = set(nums), 0

    while len(s) > 0:
        i, l = s.pop(), 1

        t = i
        while t+1 in s:
            s.remove(t+1)
            t, l = t+1, l+1

        t = i 
        while t-1 in s:
            s.remove(t-1)
            t, l = t-1, l+1
        ml = max(l, ml)

    return ml



