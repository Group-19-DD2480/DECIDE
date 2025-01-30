from decision_logic import Calculate_Launch

def test_launch() -> None:
    """
    The final launch/no launch decision is based on the FUV. The decision to launch requires that all
    elements in the FUV be true, i.e. LAUNCH should be set to true if and only if FUV[i] is true for
    all i, 0 ≤ i ≤ 14. For the example, LAUNCH is false because FUV[0] is false.
    """

    true_row = [True for _ in range(15)]
    assert Calculate_Launch(true_row)
    false_row = [False for _ in range(15)]
    assert not Calculate_Launch(false_row)
    mixed_row = [True for _ in range(7)] + [False for _ in range(8)]
    assert not Calculate_Launch(mixed_row)

def test_launch_invalid_length() -> None:
    short_row = [True for _ in range(14)]
    assert not Calculate_Launch(short_row)
