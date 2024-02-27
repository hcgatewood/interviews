from pytest import approx
from src import price_billboard


def test():
    assert price_billboard("a", {"a": 2}) == approx(2)
    assert price_billboard("a", {"b": 3}) is None

    assert price_billboard("a", {"a": 2, "aa": 4}) == approx(2)
    assert price_billboard("a", {"ab": 10}) is None
    assert price_billboard("a", {"ab": 10, "aabb": 20}) is None
    assert price_billboard("a", {"a": 2, "b": 3, "c": 4}) == approx(2)
    assert price_billboard("a", {"a": 2, "b": 3, "c": 4, "d": 5, "aa": 4}) == approx(2)

    assert price_billboard("abcd", {"ab": 10, "cde": 15, "e": 5}) == approx(20)
    assert price_billboard("abcd", {"ab": 10, "cde": 15, "ee": 10}) == approx(20)
    assert price_billboard("abcdx", {"ab": 10, "cde": 15, "e": 5}) is None
    assert price_billboard("abcd", {"ab": 10, "cdecde": 15, "e": 5}) == approx(12.5)
    assert price_billboard("abcd", {"ab": 0, "cde": 7.5, "e": 5}) == approx(2.5)

    assert price_billboard("abcd", {"ab": -10, "cde": 7.5, "e": 5}) == approx(-7.5)
    assert price_billboard("abcd", {"ab": -10, "cde": 7.5, "e": -5}) == approx(2.5)

    assert price_billboard("ab", {"a": 2, "b": 3}) == approx(5)
    assert price_billboard("aabcc", {"a": 2, "b": 3, "c": 4}) == approx(15)
    assert price_billboard("aabb", {"ab": 5}) == approx(10)
    assert price_billboard("aabcd", {"aa": 2, "ab": 10, "cde": 15, "e": 5}) == approx(21)

    assert price_billboard(
        "ggffeeedddcccbbbaaaa",
        {
            "abcdefg": 277,
            "aabbccc": 108,
            "bdddeee": 311,
            "aaagggg": 207,
            "eeeefgg": 511,
            "aabbegg": 210,
            "aacceeg": 280,
        },
    ) == approx(711)
