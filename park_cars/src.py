"""
Find the minimum fuel required to park n cars horizontally, given positions sorted by x coordinate.
"""

DEBUG = False

XY = tuple[float, float]
Result = tuple[list[float], float]


def park_cars(*cars: XY) -> float:
    x, cost_x = find_x([c[0] for c in cars])
    y, cost_y = find_y([c[1] for c in cars])
    cost = cost_x + cost_y
    if DEBUG:
        print(f"{cost_x}+{cost_y}={cost}", *cars, "->", *list(zip(x, y)))
    return cost


def find_x(vals: list[float]) -> Result:
    if not vals:
        return [], 0
    costs = [i - v for i, v in enumerate(vals)]
    median = find_median(costs)
    x = [i - median for i in range(len(vals))]
    cost = sum(abs(c - median) for c in costs)
    return x, cost


def find_y(vals: list[float]) -> Result:
    if not vals:
        return [], 0
    median = find_median(vals)
    y = [median for _ in vals]
    cost = sum(abs(v - median) for v in vals)
    return y, cost


def find_median(vals: list[float]) -> float:
    if len(vals) % 2 == 1:
        return quickselect(vals, len(vals) // 2)
    else:
        a = quickselect(vals, len(vals) // 2 - 1)
        b = quickselect(vals, len(vals) // 2)
        return (a + b) / 2


def quickselect(vals: list[float], k: int) -> float:
    if len(vals) == 1:
        return vals[0]

    pivot = vals[0]

    left = [v for v in vals if v < pivot]
    right = [v for v in vals if v > pivot]
    n_pivots = sum(1 for v in vals if v == pivot)

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + n_pivots:
        return pivot
    else:
        return quickselect(right, k - len(left) - n_pivots)
