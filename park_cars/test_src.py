from src import park_cars


def test():
    assert park_cars() == 0
    assert park_cars((1, 1)) == 0
    assert park_cars((1, 1), (2, 1)) == 0

    assert park_cars((1, 1), (2, 2)) == 1
    assert park_cars((1, 1), (4, 4)) == 5

    assert park_cars((-4, -4), (1, 5), (4, -1), (4, -5), (6, 1)) == 23
