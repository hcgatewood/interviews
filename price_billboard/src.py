"""
Determine the price of a billboard, given the prices of existing billboards.
"""

from typing import Optional

import numpy as np
from numpy.typing import NDArray

Arr = NDArray[np.floating]


def price_billboard(s: str, prices: dict[str, float]) -> Optional[float]:
    alphabet = make_alphabet(s, *prices.keys())
    x, error = solve(alphabet, s, prices)
    if error:
        return None
    price = np.dot(x.flatten(), np.array(list(prices.values())))
    return price


def solve(alphabet: list[str], s: str, prices: dict[str, float]) -> tuple[Optional[Arr], str]:
    a = make_freq(alphabet, *prices.keys())
    b = make_freq(alphabet, s)
    x, _, _, _ = np.linalg.lstsq(a, b, rcond=None)
    if not np.allclose(a @ x, b):
        return None, "no solution"
    return x, ""


def make_freq(alphabet: list[str], *strs: str) -> Arr:
    arr = np.zeros((len(alphabet), len(strs)), np.float64)
    for i, s in enumerate(strs):
        for c in s:
            arr[alphabet.index(c), i] += 1
    return arr


def make_alphabet(*strs: str) -> list[str]:
    return sorted({c for s in strs for c in s})
