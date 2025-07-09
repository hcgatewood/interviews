"""
Build a DAG and report the sum of a vertex's descendants.
"""

from collections import Counter, defaultdict
from typing import DefaultDict, Protocol

K = str
V = int


class DAGSum(Protocol):
    def get_value(self, key: K) -> V: ...
    def set_value(self, key: K, value: V): ...
    def set_sum(self, key: K, values: list[K]): ...


class DAGSumWriteOptimized:
    vals: DefaultDict[K, V]
    children: DefaultDict[K, Counter[K]]

    def __init__(self):
        self.vals = defaultdict(int)
        self.children = defaultdict(Counter)

    def get_value(self, key: str) -> int:
        if not self.children[key]:
            return self.vals[key]
        return sum(self.get_value(child) * mult for child, mult in self.children[key].items())

    def set_value(self, key: str, value: int):
        self.vals[key] = value
        self.children[key] = Counter()

    def set_sum(self, key: str, values: list[str]):
        self.vals[key] = 0
        self.children[key] = Counter(values)


class DAGSumReadOptimized:
    vals: DefaultDict[K, V]
    children: DefaultDict[K, Counter[K]]
    parents: DefaultDict[K, set[K]]

    def __init__(self):
        self.vals = defaultdict(int)
        self.children = defaultdict(Counter)
        self.parents = defaultdict(set)

    def get_value(self, key: str) -> int:
        return self.vals[key]

    def set_value(self, key: str, value: int):
        self._fix_ptrs(key, [])
        self._set_value(key, value)

    def set_sum(self, key: str, values: list[str]):
        self._fix_ptrs(key, values)
        self._set_value(key, sum(self.vals[child] * mult for child, mult in self.children[key].items()))

    def _fix_ptrs(self, key: str, values: list[str]):
        for child in self.children[key]:
            self.parents[child].remove(key)
        self.children[key] = Counter(values)
        for child in self.children[key]:
            self.parents[child].add(key)

    def _set_value(self, key: str, value: int):
        delta = value - self.vals[key]
        if delta == 0:
            return
        self.vals[key] = value
        if not self.parents[key]:
            return
        for parent in self.parents[key]:
            mult = self.children[parent][key]
            inc = delta * mult
            self._set_value(parent, self.vals[parent] + inc)
