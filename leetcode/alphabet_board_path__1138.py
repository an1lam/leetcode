"""
My initial idea: break the target string into a deduped list of character, number pairs.

Iterate through this list and use BFS to find the shortest path from the current
character to the next character.
"""

from collections import Counter
from collections import deque
from typing import List
from typing import Tuple


board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
NEIGHBOR_IDXS = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}


def within_bounds(coord):
    x, y = coord
    return y < len(board) and y >= 0 and x >= 0 and x < len(board[y])


def board_bfs(src: Tuple[int, int], target: str):
    visited = set()
    steps = {}
    q = deque([(src, None)])

    dst = None
    while len(q) > 0 and dst is None:
        curr, step = q.pop()

        if within_bounds(curr) and curr not in visited:
            steps[curr] = step
            visited.add(curr)

            if board[curr[1]][curr[0]] == target:
                dst = curr
            else:
                for s, (h, v) in NEIGHBOR_IDXS.items():
                    q.appendleft(((curr[0] + h, curr[1] + v), s))

    step = steps[dst]
    path = []
    move = NEIGHBOR_IDXS.get(step)
    prev = dst
    while step is not None:
        move = NEIGHBOR_IDXS[step]
        prev = (prev[0] - move[0], prev[1] - move[1])
        path.append(step)
        step = steps[prev]
    path.reverse()
    return path, dst


def alphabet_board_path_slow(target: str) -> str:
    src = (0, 0)
    path = []
    for char in target:
        curr_path, src = board_bfs(src, char)
        curr_path.append("!")
        path.extend(curr_path)
    return "".join(path)

def alphabet_board_path(target: str) -> str:
    curr_x, curr_y = (0, 0)
    
    path = []
    for c in target:
        dst_x = (ord(c) - ord('a')) % 5
        dst_y = (ord(c) - ord('a')) // 5

        x_first = (c == "z")
        
        x_move = 'R' if curr_x < dst_x else 'L'
        y_move = 'D' if curr_y < dst_y else 'U'
        if x_first:
            path.extend([x_move] * abs(dst_x - curr_x))
            path.extend([y_move] * abs(dst_y - curr_y))
        else:
            path.extend([y_move] * abs(dst_y - curr_y))
            path.extend([x_move] * abs(dst_x - curr_x))

        curr_x, curr_y = dst_x, dst_y
        path.append('!')
    return "".join(path)
