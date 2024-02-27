from src import find_reachable


def test():
    assert sorted(find_reachable([[0 for _ in range(6)] for _ in range(6)], (2, 0))) == [
        (0, 0),
        (0, 2),
        (1, 0),
        (1, 1),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
        (2, 5),
        (3, 0),
        (3, 1),
        (4, 0),
        (4, 2),
        (5, 0),
        (5, 3),
    ]

    assert sorted(find_reachable([[0 for _ in range(6)] for _ in range(6)], (2, 2))) == [
        (0, 0),
        (0, 2),
        (0, 4),
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 0),
        (2, 1),
        (2, 3),
        (2, 4),
        (2, 5),
        (3, 1),
        (3, 2),
        (3, 3),
        (4, 0),
        (4, 2),
        (4, 4),
        (5, 2),
        (5, 5),
    ]
