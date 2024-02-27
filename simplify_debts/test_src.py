from src import Loan, Repayment, simplify_debts


def test():
    assert simplify_debts([]) == []
    assert simplify_debts(
        [
            Loan("a", {"b": 10}),
        ]
    ) == [
        Repayment("b", {"a": 10}),
    ]
    assert simplify_debts(
        [
            Loan("a", {"b": 10}),
            Loan("b", {"a": 5}),
        ]
    ) == [
        Repayment("b", {"a": 5}),
    ]

    assert (
        simplify_debts(
            [
                Loan("a", {"b": 10}),
                Loan("b", {"a": 10}),
            ]
        )
        == []
    )
    assert simplify_debts(
        [
            Loan("a", {"b": 10}),
            Loan("a", {"b": 15}),
            Loan("a", {"b": 25}),
            Loan("b", {"a": 2}),
            Loan("b", {"a": 3}),
        ]
    ) == [
        Repayment("b", {"a": 45}),
    ]
    assert simplify_debts(
        [
            Loan("c", {"a": 1}),
            Loan("c", {"b": 1}),
            Loan("b", {"a": 1}),
        ]
    ) == [
        Repayment("a", {"c": 2}),
    ]

    # Ref: https://medium.com/@mithunmk93/algorithm-behind-splitwises-debt-simplification-feature-8ac485e97688
    assert simplify_debts(
        [
            Loan("a", {}),
            Loan("b", {"f": 10, "g": 30}),
            Loan("c", {"b": 40, "f": 30}),
            Loan("d", {"c": 20, "f": 10, "g": 10}),
            Loan("e", {"d": 50, "f": 10}),
            Loan("f", {}),
            Loan("g", {}),
        ]
    ) == [
        Repayment("b", {"c": 10}),
        Repayment("d", {"e": 40}),
        Repayment("f", {"c": 40, "e": 20}),
        Repayment("g", {"b": 10, "d": 30}),
    ]
