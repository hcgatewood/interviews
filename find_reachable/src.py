"""
Find the squares a queen can reach on a chessboard.
"""

from itertools import product

XY = tuple[int, int]


def find_reachable(board: list[list[int]], position: XY) -> list[XY]:
    reachable = []
    directions = (d for d in product([-1, 0, 1], repeat=2) if d != (0, 0))
    for direction in directions:
        cur = add_wise(position, direction)
        while is_inbounds(cur, len(board), len(board[0])):
            reachable.append(cur)
            cur = add_wise(cur, direction)
    return reachable


def is_inbounds(current: XY, nrows: int, ncols: int) -> bool:
    return 0 <= current[0] < nrows and 0 <= current[1] < ncols


def add_wise(a: XY, b: XY) -> XY:
    return a[0] + b[0], a[1] + b[1]
