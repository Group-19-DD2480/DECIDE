import math
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from lic import *



"""
There exists at least one set of two consecutive data points that are a distance greater than
the length, LENGTH1, apart.
(0 ≤ LENGTH1)
"""
def test_lic_0_positive() -> None:
    # Valid test case: Condition is true (distance > LENGTH1)
    points = [(0, 0), (0, 5), (10, 10), (100, 100)]
    length_1 = 2
    assert lic_0(points, length_1)

def test_lic_0_negative() -> None:
    # Invalid test case: Condition is false (distance ≤ LENGTH1)
    points = [(0, 0), (0, 1)]
    length_1 = 2
    assert not lic_0(points, length_1)

def test_lic_0_invalid() -> None:
    # Single point: (raises exception)
    points = [(0, 0)]
    length_1 = 2
    assert not lic_0(points, length_1)


"""
There exists at least one set of three consecutive data points
that cannot all be contained within or on a circle of radius RADIUS1.
(0 ≤ RADIUS1)
"""
def test_lic_1_positive() -> None:
    # Too small radius
    points = [(0, 0), (0, 2), (1, 1)]
    radius = 0.5
    assert lic_1(points, radius)

    # Two overlapping sets, none uncontainable
    points = [(-1, 2), (0, 0), (0, 2), (1, 2)]
    radius = 1
    assert lic_1(points, radius)

    # Two overlapping sets, one uncontainable
    points = [(-1, 1), (0, 0), (0, 2), (1, 2)]
    radius = 1
    assert lic_1(points, radius)

def test_lic_1_negative() -> None:

    # Exact radius
    points = [(0, 0), (0, 2), (1, 1)]
    radius = 1
    assert not lic_1(points, radius)

    # Exact radius acute triangle
    points = [(0, 1), (1, 0), (-1/math.sqrt(2), -1/math.sqrt(2))]
    radius = 1
    assert not lic_1(points, radius)

    # Larger radius
    points = [(0, 0), (0, 2), (1, 1)]
    radius = 2
    assert not lic_1(points, radius)

    # Two overlapping sets, both containable
    points = [(-1, 1), (0, 0), (0, 2), (1, 1)]
    radius = 1
    assert not lic_1(points, radius)

def test_lic_1_invalid() -> None:
    # Invalid radius
    points = [(0, 0), (0, 2), (1, 1)]
    radius = -1
    assert not lic_1(points, radius)

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
def test_lic_2_positive() -> None:
    # Correct angles
    points = [(1, 0), (0, 0), (0, 1)]
    assert lic_2(points, 0)
    assert lic_2(points, 0.5)

    # Multiple points
    points = [(0, 0), (2, 0), (0, 0), (0, 2)]
    assert lic_2(points, 0)
    assert lic_2(points, 0.5)

def test_lic_2_negative() -> None:
    # Invalid angles
    points = [(0, 0), (1, 0), (0, 0)]
    assert not lic_2(points, 0)
    points = [(1, 0), (0, 0), (0, 1)]
    assert not lic_2(points, math.pi / 2)


'''
There exists at least one set of three consecutive data points that
are the vertices of a triangle with area greater than AREA1.
(0 <= AREA1)
'''
def test_lic_3_positive() -> None:
    # Traingle is larger than area
    area = 1.0
    points = [(0, 0), (3, 0), (0, 3)]
    assert lic_3(points, area)

def test_lic_3_negative() -> None:
    # Exact area
    area = 1.0
    points = [(0, 0), (2, 0), (0, 1)]
    assert not lic_3(points, area)

def test_lic_3_invalid() -> None:
    # Invalid area 
    area = -1.0
    points = [(0, 0), (0, 1), (1, 2)]
    assert not lic_3(points, area)


'''
There exists at least one set of Q_PTS consecutive data points that lie in more than QUADS
quadrants. Where there is ambiguity as to which quadrant contains a given point, priority
of decision will be by quadrant number, i.e., I, II, III, IV. For example, the data point (0,0)
is in quadrant I, the point (-1,0) is in quadrant II, the point (0,-1) is in quadrant III, the point
(0,1) is in quadrant I and the point (1,0) is in quadrant I.
(2 <= Q_PTS <= NUMPOINTS),(1 <= QUADS <= 3)
'''
def test_lic_4_positive() -> None:
    # Sufficient points in multiple quadrants
    q_pts = 4
    quads = 2
    points = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    assert lic_4(points, q_pts, quads)

    # Exactly the required number of quadrants
    q_pts = 3
    quads = 2
    points = [(1, 1), (-1, 1), (-1, -1)]
    assert lic_4(points, q_pts, quads)

def test_lic_4_negative() -> None:
    # All points in a single quadrant
    q_pts = 3
    quads = 1
    points = [(1, 1), (2, 2), (3, 3), (4, 4)]
    assert not lic_4(points, q_pts, quads)

def test_lic_4_invalid() -> None:
    # Not enough consecutive points
    q_pts = 5
    quads = 3
    points = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    assert not lic_4(points, q_pts, quads)

    # Q_PTS too small
    q_pts = 1
    quads = 1
    points = [(1, 1), (2, 2)]
    assert not lic_4(points, q_pts, quads)

    # QUADS out of range
    q_pts = 4
    quads = 4
    points = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    assert not lic_4(points, q_pts, quads)


"""
There exists at least one set of two consecutive data points,
(X[i],Y[i]) and (X[j],Y[j]), such
that X[j] - X[i] < 0. (where i = j-1)
"""
def test_lic_5_positive() -> None:
    points = [(1, 0), (0, 0)]
    assert lic_5(points)
    points = [(2, 3), (3, 4), (2, 4)]
    assert lic_5(points)

def test_lic_5_negative() -> None:
    points = [(0, 0), (1, 0)]
    assert not lic_5(points)
    points = [(1, 2), (3, 4), (4, 5)]
    assert not lic_5(points)

def test_lic_5_invalid() -> None:
    #too few points
    points = [(0, 0)]
    assert not lic_5(points)


"""
There exists at least one set of N PTS consecutive data points such that at least one of the
points lies a distance greater than DIST from the line joining the first and last of these N PTS
points. If the first and last points of these N PTS are identical, then the calculated distance
to compare with DIST will be the distance from the coincident point to all other points of
the N PTS consecutive points. The condition is not met when NUMPOINTS < 3.
(3 ≤ N PTS ≤ NUMPOINTS), (0 ≤ DIST)
"""
def test_lic_6_positive() -> None:
    points = [(0, 0), (0, 2), (1, 0)]
    n_pts = 3
    dist = 1
    assert lic_6(points, n_pts, dist)

    points = [(4, 0), (0, 0), (0, 1), (0, 2), (0, 0), (1, 0)]
    n_pts = 5
    dist = 1
    assert lic_6(points, n_pts, dist)

    #coincident points
    points = [(0, 0), (2, 0), (0, 0)]
    n_pts = 3
    dist = 1
    assert lic_6(points, n_pts, dist)
    
def test_lic_6_negative() -> None:
    points = [(0, 0), (0, 1), (1, 0)]
    n_pts = 3
    dist = 2
    assert not lic_6(points, n_pts, dist)

    points = [(4, 0), (0, 0), (0, 1), (1, 1), (0, 0), (1, 0)]
    n_pts = 5
    dist = 2
    assert not lic_6(points, n_pts, dist)

    #exact distance
    points = [(0, 0), (0, 2), (1, 0)]
    n_pts = 3
    dist = 2
    assert not lic_6(points, n_pts, dist)

    #coincident point
    points = [(0, 0), (1, 0), (0, 0)]
    n_pts = 3
    dist = 2
    assert not lic_6(points, n_pts, dist)

    #exact distance
    points = [(0, 0), (1, 0), (0, 0)]
    n_pts = 3
    dist = 1
    assert not lic_6(points, n_pts, dist)

def test_lic_6_invalid() -> None:
    #too few points
    points = [(0, 0), (1, 2)]
    n_pts = 2
    dist = 1
    assert not lic_6(points, n_pts, dist)

    #too large n_pts
    points = [(0, 0), (0, 2), (1, 0)]
    n_pts = 4
    dist = 1
    assert not lic_6(points, n_pts, dist)

    #negative distance
    points = [(0, 0), (0, 2), (1, 0)]
    n_pts = 3
    dist = -1
    assert not lic_6(points, n_pts, dist)


"""
Determines if there exists at least one set of two data points separated by exactly
k_pts consecutive intervening points that are a euclidean_dist greater than length_1 apart.
"""
def test_lic_7_positive() -> None:
    # Condition met (distance > length_1)
    points = [(0, 0), (1, 1), (6, 6), (10, 10)]
    k_pts = 1
    length_1 = 5
    assert lic_7(points, k_pts, length_1)

def test_lic_7_negative() -> None:
    # Condition not met (all distances <= length_1)
    points = [(0, 0), (1, 1), (2, 2), (3, 3)]
    k_pts = 1
    length_1 = 5
    assert not lic_7(points, k_pts, length_1)

    # Distance exactly equal to length_1 (not > length_1)
    points = [(0, 0), (1, 1), (2, 2)]
    k_pts = 1
    length_1 = np.sqrt(8)  # sqrt((2-0)^2 + (2-0)^2) = sqrt(8)
    assert not lic_7(points, k_pts, length_1)

def test_lic_7_invalid() -> None:
    # NUMPOINTS < 3 (invalid case)
    points = [(0, 0), (1, 1)]
    k_pts = 1
    length_1 = 1
    assert not lic_7(points, k_pts, length_1)

    # Invalid k_pts (k_pts > NUMPOINTS - 2)
    points = [(0, 0), (2, 1), (2, 5), (3, 3)]
    k_pts = 3
    length_1 = 1
    assert not lic_7(points, k_pts, length_1)

    # Invalid k_pts (k_ps < 1)
    points = [(0, 0), (1, 1), (2, 0), (3, 4)]
    k_pts = 0
    length_1 = 1
    assert not lic_7(points, k_pts, length_1)


'''
There exists at least one set of three data points separated by exactly A PTS and B PTS
consecutive intervening points, respectively, that cannot be contained within or on a circle of
radius RADIUS1. The condition is not met when NUMPOINTS < 5.
1 ≤ A PTS, 1 ≤ B PTS
A PTS+B PTS ≤ (NUMPOINTS−3)
'''
def test_lic_8_positive() -> None:
    # Too small radius
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius = 0.5
    a_pts = 1
    b_pts = 1
    assert lic_8(points, radius, a_pts, b_pts)

    # Two sets, none containable
    points = [(-1, 2), (0, 0), (0, 0), (0, 2), (0, 2), (1, 2)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert lic_8(points, radius, a_pts, b_pts)

    # Two overlapping sets, one uncontainable
    points = [(-1, 2), (0, 0), (0, 0), (0, 2), (0, 2), (1, 1)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert lic_8(points, radius, a_pts, b_pts)

def test_lic_8_negative() -> None:
    # Exact radius
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert not lic_8(points, radius, a_pts, b_pts)

    # Exact radius acute triangle
    points = [(0, 1), (0, 0), (1, 0), (0, 0), (-1/math.sqrt(2), -1/math.sqrt(2))]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert not lic_8(points, radius, a_pts, b_pts)

    # Larger radius
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius = 2
    a_pts = 1
    b_pts = 1
    assert not lic_8(points, radius, a_pts, b_pts)

    # Two overlapping sets, both containable
    points = [(-1, 1), (0, 0), (0, 0), (0, 2), (0, 2), (1, 1)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert not lic_8(points, radius, a_pts, b_pts)

def test_lic_8_invalid() -> None:
    # Invalid radius
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius = -1
    a_pts = 1
    b_pts = 1
    assert not lic_8(points, radius, a_pts, b_pts)

    # Invalid a_pts
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius = 1
    a_pts = -1
    b_pts = 1
    assert not lic_8(points, radius, a_pts, b_pts)

    # Invalid b_pts
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius = 1
    a_pts = 1
    b_pts = -1
    assert not lic_8(points, radius, a_pts, b_pts)

    # Invalid numpoints
    points = [(0, 0), (-1, -1), (0, 2), (1, 1)]
    radius = 1
    a_pts = 1
    b_pts = 1
    assert not lic_8(points, radius, a_pts, b_pts)

    # Invalid a_pts, b_pts and numpoints combination
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius = 1
    a_pts = 2
    b_pts = 1
    assert not lic_8(points, radius, a_pts, b_pts)


"""
There exists at least one set of three data points separated by exactly C_PTS and D_PTS
consecutive intervening points, respectively, that form an angle such that:
angle < (PI-EPSILON)
or
angle > (PI+EPSILON)
The second point of the set of three points is always the vertex of the angle. If either the first
point or the last point (or both) coincide with the vertex, the angle is undefined and the LIC
is not satisfied by those three points. When NUMPOINTS < 5, the condition is not met.
1 <= C_PTS, 1 <= D_PTS
C_PTS + D_PTS <= NUMPOINTS - 3
"""
def test_lic_9_positive() -> None:
    # Basic valid case
    points = [(0, 0), (1, 2), (2, 0), (3, 1), (0, 4)]
    assert lic_9(points, 1, 1, 0.5)

def test_lic_9_negative() -> None:
    # All points are collinear
    points = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    assert not lic_9(points, 1, 1, 0.1)

    # No valid angles
    points = [(0, 0), (1, 1), (2, 0), (3, 1), (0, 4)]
    assert not lic_9(points, 1, 1, math.pi)

def test_lic_9_invalid() -> None:
    # Insufficient points
    points = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
    assert not lic_9(points[:4], 1, 1, 0.1)


"""
There exists at least one set of three data points separated by exactly E PTS and F PTS con-
secutive intervening points, respectively, that are the vertices of a triangle with area greater
than AREA1. The condition is not met when NUMPOINTS < 5.

1 ≤ E PTS, 1 ≤ F PTS
E PTS + F PTS ≤ NUMPOINTS − 3
"""
def test_lic_10_positive() -> None:
    # Valid area
    points = [(0, 0), (0, 0), (0, 2), (1, 0), (4, 0), (0, 2)]
    e_pts = 1
    f_pts = 1
    area = 1
    assert lic_10(points, e_pts, f_pts, area)

def test_lic_10_negative() -> None:
    # Exact area
    points = [(0, 0), (0, 0), (1, 0), (1, 0), (0, 2), (0, 2)]
    e_pts = 1
    f_pts = 1
    area = 1
    assert not lic_10(points, e_pts, f_pts, area)

def test_lic_10_invalid() -> None:
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

    # Invalid area
    points = [(0, 0), (0, 0), (0, 2), (1, 0), (4, 0), (0, 2)]
    e_pts = 1
    f_pts = 1
    area = -1
    assert not lic_10(points, e_pts, f_pts, area)


"""
There exists at least one set of two data points, (X[i],Y[i]) and (X[j],Y[j]), separated by
exactly G PTS consecutive intervening points, such that X[j] - X[i] < 0. (where i < j ) The
condition is not met when NUMPOINTS < 3.

1 ≤ G PTS ≤ NUMPOINTS − 2
"""
def test_lic_11_positive() -> None:
    g_pts = 1
    points = [(1, 0), (2, 3), (0, 1)]
    assert lic_11(points, g_pts)

    g_pts = 2
    points = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 6)]
    assert lic_11(points, g_pts)

def test_lic_11_negative() -> None:
    g_pts = 1
    points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    assert not lic_11(points, g_pts)

def test_lic_11_invalid() -> None:
    #NUMPOINTS < 3
    g_pts = 1
    points = [(1, 2), (0, 2)]
    assert not lic_11(points, g_pts)


"""
There exists at least one set of two data points, separated by exactly K PTS consecutive
intervening points, which are a distance greater than the length, LENGTH1, apart. In addi-
tion, there exists at least one set of two data points (which can be the same or different from
the two data points just mentioned), separated by exactly K PTS consecutive intervening
points, that are a distance less than the length, LENGTH2, apart. Both parts must be true
for the LIC to be true. The condition is not met when NUMPOINTS < 3.

0 ≤ LENGTH2
"""
def test_lic_12_positive() -> None:
    # Both conditions satisfied
    points = [(0, 0), (1, 1), (6, 6), (10, 10)]
    k_pts = 1
    length_1 = 5
    length_2 = 10
    assert lic_12(points, k_pts, length_1, length_2)

def test_lic_12_negative() -> None:
    # Condition 1 satisfied, Condition 2 not satisfied
    points = [(0, 0), (1, 1), (6, 6), (10, 10)]
    k_pts = 1
    length_1 = 5
    length_2 = 1
    assert not lic_12(points, k_pts, length_1, length_2)

    # Condition 2 satisfied, Condition 1 not satisfied
    points = [(0, 0), (1, 1), (5, 5), (3, 3)]
    k_pts = 1
    length_1 = 10
    length_2 = 3
    assert not lic_12(points, k_pts, length_1, length_2)

def test_lic_12_invalid() -> None:
    # NUMPOINTS < 3
    points = [(0, 0), (1, 1)]
    k_pts = 1
    length_1 = 5
    length_2 = 2
    assert not lic_12(points, k_pts, length_1, length_2)

    # Invalid k_pts (k_pts > NUMPOINTS - 2)
    points = [(0, 0), (2, 2), (4, 4), (6, 6)]
    k_pts = 3
    length_1 = 1
    length_2 = 2
    assert not lic_12(points, k_pts, length_1, length_2)

    # Invalid LENGTH2 (LENGTH2 < 0)
    points = [(0, 0), (1, 1), (2, 2), (3, 3)]
    k_pts = 1
    length_1 = 5
    length_2 = -1
    assert not lic_12(points, k_pts, length_1, length_2)

    # Distance exactly equal to LENGTH1 or LENGTH2 (not satisfied)
    points = [(0, 0), (1, 1), (2, 2)]
    k_pts = 1
    length_1 = math.sqrt(8)
    length_2 = math.sqrt(8)
    assert not lic_12(points, k_pts, length_1, length_2)


'''
There exists at least one set of three data points separated by exactly A PTS and B PTS
consecutive intervening points, respectively, that cannot be contained within or on a circle of
radius RADIUS1. The condition is not met when NUMPOINTS < 5.
1 ≤ A PTS, 1 ≤ B PTS
A PTS+B PTS ≤ (NUMPOINTS−3)
'''
def test_lic_13_positive() -> None:
    # Smaller radius1, exact radius 2
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = 0.5
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert lic_13(points, radius1, radius2, a_pts, b_pts)

    # Smaller radius1, larger radius 2
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = 0.5
    radius2 = 2
    a_pts = 1
    b_pts = 1
    assert lic_13(points, radius1, radius2, a_pts, b_pts)

    # Smaller radius1, exact radius2 for acute triangle
    points = [(0, 1), (0, 0), (1, 0), (0, 0), (-1/math.sqrt(2), -1/math.sqrt(2))]
    radius1 = 0.5
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert lic_13(points, radius1, radius2, a_pts, b_pts)

# Two  sets with same radius where radius1 < radius <= radius2
    points = [(-1, 1), (0, 0), (0, 0), (0, 2), (0, 2), (1, 1)]
    radius1 = 0.5
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert lic_13(points, radius1, radius2, a_pts, b_pts)

    # Two  sets with diffrent radii wehre set 1 radius <= radius1 < set 2 radius <= radius2
    points = [(-1, 1), (0, 0), (0, 0), (0, 4), (0, 2), (2, 2)]
    radius1 = 1
    radius2 = 2
    a_pts = 1
    b_pts = 1
    assert lic_13(points, radius1, radius2, a_pts, b_pts)

    # Two  sets with diffrent radii wehre set 1 radius <= radius1 <= radius2 < set 2 radius
    points = [(-1, 1), (0, 0), (0, 0), (0, 4), (0, 2), (2, 2)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert lic_13(points, radius1, radius2, a_pts, b_pts)

    # Two  sets with diffrent radii wehre  radius1 < set 1 radius <= radius2 < set 2 radius
    points = [(-1, 1), (0, 0), (0, 0), (0, 4), (0, 2), (2, 2)]
    radius1 = 0.5
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert lic_13(points, radius1, radius2, a_pts, b_pts)

def test_lic_13_negative() -> None:
# Smaller radius1, smaller radius 2
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = 0.5
    radius2 = 0.5
    a_pts = 1
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)

    # Exact radius1, larger radius 2
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = 1
    radius2 = 2
    a_pts = 1
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)
    
    # Larger radius1, larger radius 2
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = 2
    radius2 = 2
    a_pts = 1
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)
    
    # Two sets, none containable by either radius
    points = [(-1, 2), (0, 0), (0, 0), (0, 2), (0, 2), (1, 2)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)

    # Two sets, both containable by both radius
    points = [(-1, 1), (0, 0), (0, 0), (0, 2), (0, 2), (1, 1)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)

def test_lic_13_invalid() -> None:
    # Invalid radius1
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = -1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)

    # Invalid radius2
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = 1
    radius2 = -1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)

    # Invalid a_pts
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = 1
    radius2 = 1
    a_pts = -1
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)

    # Invalid b_pts
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = -1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)

    # Invalid numpoints
    points = [(0, 0), (-1, -1), (0, 2), (1, 1)]
    radius1 = 1
    radius2 = 1
    a_pts = 1
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)

    # Invalid a_pts, b_pts and numpoints combination
    points = [(0, 0), (-1, -1), (0, 2), (-2, -2), (1, 1)]
    radius1 = 1
    radius2 = 1
    a_pts = 2
    b_pts = 1
    assert not lic_13(points, radius1, radius2, a_pts, b_pts)


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
def test_lic_14_positive() -> None:
    # Traingle that accepts area 1 but not 2 and another that accepts area 2 but not 1
    points = [(0, 0), (0, 0), (2, 0), (1, 0), (0, 2), (0, 1)]
    e_pts = 1
    f_pts = 1
    area1 = 1
    area2 = 2
    assert lic_14(points, e_pts, f_pts, area1, area2)

def test_lic_14_negative() -> None:
    # Exact area1 and accepted area 2
    points = [(0, 0), (0, 0), (1, 0), (1, 0), (0, 2), (0, 2)]
    e_pts = 1
    f_pts = 1
    area1 = 1
    area2 = 3
    assert not lic_14(points, e_pts, f_pts, area1, area2)

def test_lic_14_invalid() -> None:
    # Invalid e_pts
    points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    e_pts = 0
    f_pts = 1
    area1 = 1
    area2 = 1
    assert not lic_14(points, e_pts, f_pts, area1, area2)

    # Invalid f_pts
    points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    e_pts = 1
    f_pts = 0
    area1 = 1
    area2 = 1
    assert not lic_14(points, e_pts, f_pts, area1, area2)

    # Valid area1, Invalid area2
    points = [(0, 0), (0, 0), (0, 2), (1, 0), (4, 0), (0, 2)]
    e_pts = 1
    f_pts = 1
    area1 = 1
    area2 = -1
    assert not lic_14(points, e_pts, f_pts, area1, area2)

    # Invalid area1, Valid area2
    points = [(0, 0), (0, 0), (0, 2), (1, 0), (4, 0), (0, 2)]
    e_pts = 1
    f_pts = 1
    area1 = -1
    area2 = 1
    assert not lic_14(points, e_pts, f_pts, area1, area2)
