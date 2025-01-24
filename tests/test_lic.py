import math
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from lic import *


def test_lic_7():
    """
    Tests for the lic_7 function.
    """

    # Condition met (distance > length_1)
    points = [(0, 0), (1, 1), (6, 6), (10, 10)]
    k_pts = 1
    length_1 = 5
    assert lic_7(points, k_pts, length_1) == True

    # Condition not met (all distances <= length_1)
    points = [(0, 0), (1, 1), (2, 2), (3, 3)]
    k_pts = 1
    length_1 = 5
    assert lic_7(points, k_pts, length_1) == False

    # NUMPOINTS < 3 (invalid case)
    points = [(0, 0), (1, 1)]
    k_pts = 1
    length_1 = 1
    assert lic_7(points, k_pts, length_1) == False

    # Invalid k_pts (k_pts > NUMPOINTS - 2)
    points = [(0, 0), (2, 1), (2, 5), (3, 3)]
    k_pts = 3
    length_1 = 1
    assert lic_7(points, k_pts, length_1) == False

    # Invalid k_pts (k_ps < 1)
    points = [(0, 0), (1, 1), (2, 0), (3, 4)]
    k_pts = 0
    length_1 = 1
    assert lic_7(points, k_pts, length_1) == False

    # Distance exactly equal to length_1 (not > length_1)
    points = [(0, 0), (1, 1), (2, 2)]
    k_pts = 1
    length_1 = np.sqrt(8)  # sqrt((2-0)^2 + (2-0)^2) = sqrt(8)
    assert lic_7(points, k_pts, length_1) == False


def test_lic_1() -> None:
    """
    There exists at least one set of three consecutive data points
    that cannot all be contained within or on a circle of radius RADIUS1.
    (0 ≤ RADIUS1)
    """

    # Invalid radius
    points = [(0, 0), (0, 2), (1, 1)]
    radius = -1
    assert not lic_1(points, radius)

    # Too small radius
    points = [(0, 0), (0, 2), (1, 1)]
    radius = 0.5
    assert lic_1(points, radius)

    # Exact radius
    points = [(0, 0), (0, 2), (1, 1)]
    radius = 1
    assert not lic_1(points, radius)

    # Larger radius
    points = [(0, 0), (0, 2), (1, 1)]
    radius = 2
    assert not lic_1(points, radius)

    # Two overlapping sets, none uncontainable
    points = [(-1, 2), (0, 0), (0, 2), (1, 2)]
    radius = 1
    assert lic_1(points, radius)

    # Two overlapping sets, one uncontainable
    points = [(-1, 1), (0, 0), (0, 2), (1, 2)]
    radius = 1
    assert lic_1(points, radius)

    # Two overlapping sets, both containable
    points = [(-1, 1), (0, 0), (0, 2), (1, 1)]
    radius = 1
    assert not lic_1(points, radius)


def test_lic_2() -> None:
    """
    There exists at least one set of three consecutive data points which form an angle such that:
    angle < (PI - EPSILON)
    or
    angle > (PI + EPSILON)
    The second of the three consecutive points is always the vertex of the angle. If either the first
    point or the last point (or both) coincides with the vertex, the angle is undefined and the LIC
    is not satisfied by those three points.
    (0 <= EPSILON < PI)
    """
    points = [(1, 0), (0, 0), (0, 1)]
    assert lic_2(points, 0)
    assert lic_2(points, 0.5)

    points = [(0, 0), (2, 0), (0, 0), (0, 2)]
    assert lic_2(points, 0)
    assert lic_2(points, 0.5)

    points = [(0, 0), (1, 0), (0, 0)]
    assert not lic_2(points, 0)
    points = [(1, 0), (0, 0), (0, 1)]
    assert not lic_2(points, math.pi / 2)


def test_lic_3() -> None:
    '''
    There exists at least one set of three consecutive data points that
    are the vertices of a triangle with area greater than AREA1.
    (0 <= AREA1)
    '''

    # Invalid area
    area = -1.0
    points = [(0, 0), (0, 1), (1, 2)]
    assert not lic_3(points, area)

    # Traingle is larger than area
    area = 1.0
    points = [(0, 0), (3, 0), (0, 3)]
    assert lic_3(points, area)

    # Exact area
    area = 1.0
    points = [(0, 0), (2, 0), (0, 1)]
    assert not lic_3(points, area)


def test_lic_5() -> None:
    """
    There exists at least one set of two consecutive data points,
    (X[i],Y[i]) and (X[j],Y[j]), such
    that X[j] - X[i] < 0. (where i = j-1)
    """
    points = [(1, 0), (0, 0)]
    assert lic_5(points)
    points = [(2, 3), (3, 4), (2, 4)]
    assert lic_5(points)

    points = [(0, 0), (1, 0)]
    assert not lic_5(points)
    points = [(1, 2), (3, 4), (4, 5)]
    assert not lic_5(points)
