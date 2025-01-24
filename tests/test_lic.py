import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from lic import *


def test_lic_0() -> None:
    """
    There exists at least one set of two consecutive data points that are a distance greater than
    the length, LENGTH1, apart.
    (0 ≤ LENGTH1)
    """

    # Valid test case
    points = [(0, 0), (0, 1), (0, 2), (0, 3)]
    length_1 = 2
    assert lic_0(points, length_1) == True

    # Invalid test case
    points = [(0, 0), (0, 5), (10, 10), (100, 100)]
    length_1 = 2
    assert lic_0(points, length_1) == False

    # Single point
    points = [(0, 0)]
    length_1 = 2
    assert lic_0(points, length_1) == False
