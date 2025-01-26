import math
import numpy as np
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

    # Invalid test case: Condition is false (distance ≤ LENGTH1)
    points = [(0, 0), (0, 1)]
    length_1 = 2
    assert not lic_0(points, length_1)

    # Valid test case: Condition is true (distance > LENGTH1)
    points = [(0, 0), (0, 5), (10, 10), (100, 100)]
    length_1 = 2
    assert lic_0(points, length_1)

    # Single point: (raises exception)
    points = [(0, 0)]
    length_1 = 2
    assert not lic_0(points, length_1)

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
    # Correct angles
    points = [(1, 0), (0, 0), (0, 1)]
    assert lic_2(points, 0)
    assert lic_2(points, 0.5)

    # Multiple points
    points = [(0, 0), (2, 0), (0, 0), (0, 2)]
    assert lic_2(points, 0)
    assert lic_2(points, 0.5)

    # Invalid angles
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

def test_lic_4() -> None:
    '''
    There exists at least one set of Q_PTS consecutive data points that lie in more than QUADS
    quadrants. Where there is ambiguity as to which quadrant contains a given point, priority
    of decision will be by quadrant number, i.e., I, II, III, IV. For example, the data point (0,0)
    is in quadrant I, the point (-1,0) is in quadrant II, the point (0,-1) is in quadrant III, the point
    (0,1) is in quadrant I and the point (1,0) is in quadrant I.
    (2 <= Q_PTS <= NUMPOINTS),(1 <= QUADS <= 3)

    '''

    # Sufficient points in multiple quadrants
    points = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    assert lic_4(points, q_pts=4, quads=2)

    # All points in a single quadrant
    points = [(1, 1), (2, 2), (3, 3), (4, 4)]
    assert not lic_4(points, q_pts=3, quads=1)

    # Exactly the required number of quadrants
    points = [(1, 1), (-1, 1), (-1, -1)]
    assert lic_4(points, q_pts=3, quads=2)

    # Not enough consecutive points
    points = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    assert not lic_4(points, q_pts=5, quads=3)

    # Q_PTS too small
    points = [(1, 1), (2, 2)]
    assert not lic_4(points, q_pts=1, quads=1)

    # QUADS out of range
    points = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    assert not lic_4(points, q_pts=4, quads=4)


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


def test_lic_6():
    """
    There exists at least one set of N PTS consecutive data points such that at least one of the
    points lies a distance greater than DIST from the line joining the first and last of these N PTS
    points. If the first and last points of these N PTS are identical, then the calculated distance
    to compare with DIST will be the distance from the coincident point to all other points of
    the N PTS consecutive points. The condition is not met when NUMPOINTS < 3.
    (3 ≤ N PTS ≤ NUMPOINTS), (0 ≤ DIST)
    """


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

def test_lic_8() -> None:
    '''
    There exists at least one set of three data points separated by exactly A PTS and B PTS
    consecutive intervening points, respectively, that cannot be contained within or on a circle of
    radius RADIUS1. The condition is not met when NUMPOINTS < 5.
    1 ≤ A PTS, 1 ≤ B PTS
    A PTS+B PTS ≤ (NUMPOINTS−3)
    '''

    # Invalid radius
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius = -1
    a_pts = 1
    b_pts = 1
    assert not lic_8(points,radius,a_pts,b_pts)

    # Invalid a_pts
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius = 1
    a_pts = -1
    b_pts = 1
    assert not lic_8(points,radius,a_pts,b_pts)

    # Invalid b_pts
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius = 1
    a_pts = 1
    b_pts = -1
    assert not lic_8(points,radius,a_pts,b_pts)

    # Invalid numpoints
    points = [(0, 0), (-1,-1), (0, 2), (1,1)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert not lic_8(points,radius,a_pts,b_pts)

    # Invalid a_pts, b_pts and numpoints combination
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius = 1
    a_pts = 2
    b_pts = 1
    assert not lic_8(points,radius,a_pts,b_pts)

    # Too small radius
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius = 0.5
    a_pts = 1
    b_pts = 1
    assert lic_8(points,radius,a_pts,b_pts)

    # Exact radius
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert not lic_8(points,radius,a_pts,b_pts)

    # Larger radius
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius = 2
    a_pts = 1
    b_pts = 1
    assert not lic_8(points,radius,a_pts,b_pts)

    # Two sets, none containable
    points = [(-1,2), (0, 0), (0, 0), (0, 2), (0, 2), (1,2)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert lic_8(points,radius,a_pts,b_pts)

    # Two overlapping sets, one uncontainable
    points = [(-1,2), (0, 0), (0, 0), (0, 2), (0, 2), (1,1)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert lic_8(points,radius,a_pts,b_pts)

    # Two overlapping sets, both containable
    points = [(-1,1), (0, 0), (0, 0), (0, 2), (0, 2), (1,1)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert not lic_8(points,radius,a_pts,b_pts)

def test_lic_9():
    """
    There exists at least one set of three data points separated by exactly C PTS and D PTS
    consecutive intervening points, respectively, that form an angle such that:

    angle < (PI − EPSILON)
    or
    angle > (PI + EPSILON)

    The second point of the set of three points is always the vertex of the angle. If either the first
    point or the last point (or both) coincide with the vertex, the angle is undefined and the LIC
    is not satisfied by those three points. When NUMPOINTS < 5, the condition is not met.

    1 ≤ C PTS, 1 ≤ D PTS
    C PTS + D PTS ≤ NUMPOINTS − 3
    """


def test_lic_10():
    """
    There exists at least one set of three data points separated by exactly E PTS and F PTS con-
    secutive intervening points, respectively, that are the vertices of a triangle with area greater
    than AREA1. The condition is not met when NUMPOINTS < 5.

    1 ≤ E PTS, 1 ≤ F PTS
    E PTS + F PTS ≤ NUMPOINTS − 3
    """
    # Invalid e_pts
    points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    e_pts = 0
    f_pts = 1
    area = 1
    assert not lic_10(points, e_pts, f_pts, area)

    # Invalid f_pts
    points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    e_pts = 1
    f_pts = 0
    area = 1
    assert not lic_10(points, e_pts, f_pts, area)

    # Valid area
    points = [(0, 0), (0, 0), (0, 2), (1, 0), (4, 0), (0, 2)]
    e_pts = 1
    f_pts = 1
    area = 1
    assert  lic_10(points, e_pts, f_pts, area)

    # Exact area
    points = [(0, 0), (0, 0), (1, 0), (1, 0), (0, 2), (0, 2)]
    e_pts = 1
    f_pts = 1
    area = 1
    assert  not lic_10(points, e_pts, f_pts, area)


def test_lic_11():
    """
    There exists at least one set of two data points, (X[i],Y[i]) and (X[j],Y[j]), separated by
    exactly G PTS consecutive intervening points, such that X[j] - X[i] < 0. (where i < j ) The
    condition is not met when NUMPOINTS < 3.

    1 ≤ G PTS ≤ NUMPOINTS − 2
    """


def test_lic_12():
    """
    There exists at least one set of two data points, separated by exactly K PTS consecutive
    intervening points, which are a distance greater than the length, LENGTH1, apart. In addi-
    tion, there exists at least one set of two data points (which can be the same or different from
    the two data points just mentioned), separated by exactly K PTS consecutive intervening
    points, that are a distance less than the length, LENGTH2, apart. Both parts must be true
    for the LIC to be true. The condition is not met when NUMPOINTS < 3.

    0 ≤ LENGTH2
    """

def test_lic_13() -> None:

    '''
    There exists at least one set of three data points separated by exactly A PTS and B PTS
    consecutive intervening points, respectively, that cannot be contained within or on a circle of
    radius RADIUS1. The condition is not met when NUMPOINTS < 5.
    1 ≤ A PTS, 1 ≤ B PTS
    A PTS+B PTS ≤ (NUMPOINTS−3)
    '''

    # Invalid radius1
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = -1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)

    # Invalid radius2
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = 1
    radius2 = -1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)

    # Invalid a_pts
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = 1
    radius2 = 1
    a_pts = -1
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)

    # Invalid b_pts
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = -1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)

    # Invalid numpoints
    points = [(0, 0), (-1,-1), (0, 2), (1,1)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)

    # Invalid a_pts, b_pts and numpoints combination
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = 1
    radius2 = 1
    a_pts = 2
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)
    
    # Smaller radius1, smaller radius 2
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = 0.5
    radius2 = 0.5
    a_pts = 1
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)

    # Smaller radius1, exact radius 2
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = 0.5
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert lic_13(points,radius1,radius2,a_pts,b_pts)

    # Smaller radius1, larger radius 2
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = 0.5
    radius2 = 2
    a_pts = 1
    b_pts = 1
    assert lic_13(points,radius1,radius2,a_pts,b_pts)
    
    # Exact radius1, larger radius 2
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = 1
    radius2 = 2
    a_pts = 1
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)
    
    # Larger radius1, larger radius 2
    points = [(0, 0), (-1,-1), (0, 2), (-2,-2), (1,1)]
    radius1 = 2
    radius2 = 2
    a_pts = 1
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)

    # Two sets, none containable by either radius
    points = [(-1,2), (0, 0), (0, 0), (0, 2), (0, 2), (1,2)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)

    # Two sets, both containable by both radius
    points = [(-1,1), (0, 0), (0, 0), (0, 2), (0, 2), (1,1)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points,radius1,radius2,a_pts,b_pts)

    # Two  sets with same radius where radius1 < radius <= radius2
    points = [(-1,1), (0, 0), (0, 0), (0, 2), (0, 2), (1,1)]
    radius1 = 0.5
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert lic_13(points,radius1,radius2,a_pts,b_pts)

    # Two  sets with diffrent radii wehre set 1 radius <= radius1 < set 2 radius <= radius2
    points = [(-1,1), (0, 0), (0, 0), (0, 4), (0, 2), (2,2)]
    radius1 = 1
    radius2 = 2
    a_pts = 1
    b_pts = 1
    assert lic_13(points,radius1,radius2,a_pts,b_pts)

    # Two  sets with diffrent radii wehre set 1 radius <= radius1 <= radius2 < set 2 radius
    points = [(-1,1), (0, 0), (0, 0), (0, 4), (0, 2), (2,2)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert lic_13(points,radius1,radius2,a_pts,b_pts)

    # Two  sets with diffrent radii wehre  radius1 < set 1 radius <= radius2 < set 2 radius
    points = [(-1,1), (0, 0), (0, 0), (0, 4), (0, 2), (2,2)]
    radius1 = 0.5
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert lic_13(points,radius1,radius2,a_pts,b_pts)


def test_lic_14():
    """
    There exists at least one set of three data points, separated by exactly E PTS and F PTS con-
    secutive intervening points, respectively, that are the vertices of a triangle with area greater
    than AREA1. In addition, there exist three data points (which can be the same or different
    from the three data points just mentioned) separated by exactly E PTS and F PTS consec-
    utive intervening points, respectively, that are the vertices of a triangle with area less than
    AREA2. Both parts must be true for the LIC to be true. The condition is not met when:

    NUMPOINTS < 5.
    0 ≤ AREA2
    """
