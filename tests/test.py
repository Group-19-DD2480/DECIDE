import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from decide import decide
from parameters import PARAMETERS_T


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
