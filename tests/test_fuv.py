
from decision_logic import Calculate_FUV

def test_fuv() -> None:
    """
    The Final Unlocking Vector (FUV) is generated from the Preliminary Unlocking Matrix. The
    input PUV indicates whether the corresponding LIC is to be considered as a factor in signaling
    interceptor launch. FUV[i] should be set to true if PUV[i] is false (indicating that the associated
    LIC should not hold back launch) or if all elements in PUM row i are true.
    """

    # Indices 0, 1 and 4+ should be true because PUV is false
    # Index 2 should be false because PUV is true but not all PUM entries in the row are true
    # Index 3 should be true because PUV is true and all PUM entries in the row are true
    true_row = [True for _ in range(15)]
    false_row = [False for _ in range(15)]
    mixed_row = [True for _ in range(7)] + [False for _ in range(8)]
    PUM = [true_row,false_row,mixed_row,true_row]+ [true_row for _ in range(11)]
    PUV = [False,False,True,True]+ [False for _ in range(11)]
    expected_FUV = [True,True,False,True]+ [True for _ in range(11)]

    assert (Calculate_FUV(PUM,PUV) == expected_FUV).all()