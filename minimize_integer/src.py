"""
Find the minimum integer possible making at most k swaps.
"""

from collections import defaultdict
from typing import Optional


class Fenwick:
    def __init__(self, n):
        self.nums = [0] * n

    @staticmethod
    def lsb(i: int) -> int:
        return i & -i

    def update_point(self, i: int, delta: int) -> None:
        i += 1
        while i < len(self.nums):
            self.nums[i - 1] += delta
            i += self.lsb(i)

    def query_point(self, i: int) -> int:
        i += 1
        val = 0
        while i > 0:
            val += self.nums[i - 1]
            i -= self.lsb(i)
        return val


def minimize_integer(num: str, k: int) -> str:
    n = len(num)
    digit_to_idxs = defaultdict(list)
    for i in range(n - 1, -1, -1):
        digit_to_idxs[int(num[i])].append(i)

    prefix = []
    fenwick = Fenwick(n)
    removed = set()

    while k:
        d, cost = find_best(digit_to_idxs, fenwick, k)
        if d is None:
            break
        k -= cost
        prefix.append(d)
        i = digit_to_idxs[d].pop()
        fenwick.update_point(i, 1)
        removed.add(i)

    left = "".join(str(d) for d in prefix)
    right = "".join(num[i] for i in range(n) if i not in removed)
    return left + right


def find_best(digits_to_idxs: dict[int, list[int]], fenwick: Fenwick, k: int) -> tuple[Optional[int], Optional[int]]:
    for d in range(10):
        if not digits_to_idxs[d]:
            continue
        i = digits_to_idxs[d][-1]
        cost = i - fenwick.query_point(i)
        if cost <= k:
            return d, cost
    return None, None
