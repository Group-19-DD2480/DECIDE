from decision_logic import Calculate_Launch

"""
The final launch/no launch decision is based on the FUV. The decision to launch requires that all
elements in the FUV be true, i.e. LAUNCH should be set to true if and only if FUV[i] is true for
all i, 0 ≤ i ≤ 14. For the example, LAUNCH is false because FUV[0] is false.
"""
def test_launch_positive() -> None:
    true_row = [True for _ in range(15)]
    assert Calculate_Launch(true_row)

def test_launch_negative() -> None:
    false_row = [False for _ in range(15)]
    assert not Calculate_Launch(false_row)
    
    mixed_row = [True for _ in range(7)] + [False for _ in range(8)]
    assert not Calculate_Launch(mixed_row)
