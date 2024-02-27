from src import merge_lists


def test():
    assert merge_lists([]) == []
    assert merge_lists([], []) == []
    assert merge_lists([], [], [(1, 10)]) == [(1, 10)]
    assert merge_lists([(-1, 42)]) == [(-1, 42)]
    assert merge_lists(
        [
            (1, 3),
            (5, 7),
            (9, 11),
        ],
        [
            (2, 4),
            (6, 8),
            (10, 12),
        ],
    ) == [
        (1, 4),
        (5, 8),
        (9, 12),
    ]
    assert merge_lists(
        [
            (1, 3),
            (5, 7),
            (9, 11),
        ],
        [
            (2, 4),
            (6, 8),
            (10, 12),
        ],
        [
            (1, 2),
            (3, 4),
            (5, 6),
            (7, 8),
            (9, 10),
            (11, 12),
        ],
    ) == [
        (1, 4),
        (5, 8),
        (9, 12),
    ]
    assert merge_lists(
        [
            (1, 3),
            (5, 7),
            (9, 11),
        ],
        [
            (2, 4),
            (6, 8),
            (10, 12),
        ],
        [
            (1, 2),
            (3, 4),
            (5, 6),
            (7, 8),
            (9, 10),
            (11, 12),
        ],
        [
            (1, 12),
        ],
    ) == [
        (1, 12),
    ]
