from src import minimize_integer


def test():
    assert minimize_integer("", 10) == ""
    assert minimize_integer("0", 10) == "0"
    assert minimize_integer("9", 10) == "9"

    assert minimize_integer("", 0) == ""
    assert minimize_integer("0", 0) == "0"
    assert minimize_integer("9", 0) == "9"

    assert minimize_integer("01", 10) == "01"
    assert minimize_integer("00012345", 10) == "00012345"

    assert minimize_integer("21", 0) == "21"
    assert minimize_integer("21", 1) == "12"

    assert minimize_integer("4321", 4) == "1342"
    assert minimize_integer("100", 1) == "010"
    assert minimize_integer("36789", 1000) == "36789"

    assert minimize_integer("54321", 9) == "12354"
