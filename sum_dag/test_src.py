from src import DAGSum, DAGSumReadOptimized, DAGSumWriteOptimized


def test():
    _test(DAGSumWriteOptimized())
    _test(DAGSumReadOptimized())


def _test(s: DAGSum):
    s.set_value("A", 5)
    s.set_value("B", 10)
    s.set_sum("C", ["A", "A", "B"])
    s.set_sum("D", ["C", "C", "A"])
    assert s.get_value("A") == 5
    assert s.get_value("B") == 10
    assert s.get_value("C") == 20
    assert s.get_value("D") == 45

    s.set_value("A", 100)
    assert s.get_value("D") == 520
