from decide import *
from parameters import PARAMETERS_T
import pytest

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


@pytest.fixture
def example_parameters():
    """
    Fixture to create an instance of PARAMETERS_T with default values for testing.
    """
    return PARAMETERS_T()  # Use default values specified in PARAMETERS_T


def test_decide_yes(capsys, example_parameters) -> None:
    """
    Test case where the system prints "YES".
    Only LIC_0 and LIC_1 are considered, which are satisfied by the points.
    T
    """
    points = [(0, 0), (10, 10), (20, 20), (40, 59)]  # Points satisfy LIC_0 and LIC_1
    LCM = [["ORR"] * 15 for _ in range(15)]

    PUV = [False] * 15
    PUV[0] = True  # Consider LIC_0
    PUV[1] = True  # Consider LIC_1

    decide(points, example_parameters, LCM, PUV)

    result = capsys.readouterr()

    # Assert that "YES" is printed to terminal
    assert result.out.strip() == "YES"


def test_decide_no(capsys, example_parameters) -> None:
    """
    A 'NO' case where the system outputs 'NO'.
    Points are insufficient to satisfy some LIC.
    """
    points = [(0, 0), (1, 0)]
    LCM = [["ANDD"] * 15 for _ in range(15)]
    PUV = [True] * 15

    decide(points, example_parameters, LCM, PUV)

    result = capsys.readouterr()

    # Assert that "NO" is printed to terminal
    assert result.out.strip() == "NO"
