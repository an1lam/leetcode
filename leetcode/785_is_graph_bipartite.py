from collections import deque

def bfs(graph, groups, visited, start_node):
    q = deque([(start_node, 0)])

    while len(q) > 0:
        src_node, step = q.pop() 
        if src_node not in visited:
            visited.add(src_node)
            groups[step % 2].add(src_node)

            for dst_node in graph[src_node]:
                q.appendleft((dst_node, step + 1))

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) == 0: return True
        groups = [set(), set()]
        visited = set()

        for node in range(len(graph)):
            bfs(graph, groups, visited, node)

        for group in groups:
            for src_node in group:
                for dst_node in graph[src_node]:
                    if dst_node in group:
                        return False
        return True

