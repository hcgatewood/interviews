"""
Merge k lists of n intervals.
"""

import heapq
from collections.abc import Iterable
from dataclasses import dataclass

Interval = tuple[int, int]
IntervalList = list[Interval]


@dataclass
class IntervalListHeapq:
    v: IntervalList
    idx: int = 0

    def __lt__(self, them):
        return self.v[self.idx][0] < them.v[them.idx][0]

    def get(self) -> Interval:
        return self.v[self.idx]

    def advance(self):
        self.idx += 1

    def done(self) -> bool:
        return self.idx == len(self.v)


def merge_lists(*interval_lists: IntervalList) -> IntervalList:
    merged = []
    for val in order_lists(*interval_lists):
        update_merged(merged, val)
    return merged


def order_lists(*interval_lists: IntervalList) -> Iterable[Interval]:
    heap = [IntervalListHeapq(v) for v in interval_lists if v]
    heapq.heapify(heap)
    while heap:
        v = heapq.heappop(heap)
        yield v.get()
        v.advance()
        if not v.done():
            heapq.heappush(heap, v)


def update_merged(merged: IntervalList, val: Interval):
    if merged and overlaps(merged[-1], val):
        merged[-1] = merge(merged[-1], val)
    else:
        merged.append(val)


def overlaps(a: Interval, b: Interval) -> bool:
    overlap_lo = (a[0] <= b[0]) and (b[0] <= a[1])
    overlap_hi = (a[0] <= b[1]) and (b[1] <= a[1])
    return overlap_lo or overlap_hi


def merge(a: Interval, b: Interval) -> Interval:
    interval = (
        min(a[0], b[0]),
        max(a[1], b[1]),
    )
    return interval
