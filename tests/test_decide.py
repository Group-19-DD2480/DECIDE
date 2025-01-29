from decide import *

def test_points() -> bool:
    # Num_points is length of points
    assert num_points == len(points)

    # Num_points is 2<= num_points <= 100
    assert num_points >= 2
    assert num_points <= 100


def test_lcm() -> bool:

    # Only andd, orr and notused allowed
    for row in LCM:
        for element in row:
            assert element in ["ANDD", "ORR", "NOTUSED"]

    # Height should be 15
    assert len(LCM) == 15

    # Length should be 15
    for row in LCM:
        assert len(row) == 15

    # LCM is symmetric
    for i in range(len(LCM)):
        for j in range(len(LCM[0])):
            LCM[i][j] == LCM[j][i]

def test_puv() -> bool:
    # PUV should be 15 elements
    assert len(PUV) == 15
