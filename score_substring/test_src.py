from src import score_substring


def test():
    assert score_substring("") == (0, (0, 0))
    assert score_substring("0") == (0, (0, 0))
    assert score_substring("00000") == (0, (0, 0))
    assert score_substring("1") == (1, (0, 1))
    assert score_substring("11111") == (5, (0, 5))
    assert score_substring("01") == (1, (1, 2))
    assert score_substring("10") == (1, (0, 1))
    assert score_substring("01110") == (3, (1, 4))
    assert score_substring("1011011") == (3, (2, 7))

    assert score_substring("0101110110") == (4, (3, 9))
    assert score_substring("1100101101") == (2, (0, 2))
    assert score_substring("1101111100") == (6, (0, 8))
    assert score_substring("0110110111") == (5, (1, 10))

    assert score_substring("0001101100011001011000110") == (3, (3, 8))
    assert score_substring("1100101001101110101100000") == (5, (9, 20))
