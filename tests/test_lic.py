from src.lic import *

def test_lic_2() -> None:
    '''
    There exists at least one set of three consecutive data points which form an angle such that:
    angle < (PI - EPSILON)
    or
    angle > (PI + EPSILON)
    The second of the three consecutive points is always the vertex of the angle. If either the first
    point or the last point (or both) coincides with the vertex, the angle is undefined and the LIC
    is not satisfied by those three points.
    (0 <= EPSILON < PI)
    '''
    points = [(1, 0), (0, 0), (0, 1)]
    assert lic_2(points, 0)
    assert lic_2(points, 0.5)

    points = [(0, 0), (2, 0), (0, 0), (0, 2)]
    assert lic_2(points, 0)
    assert lic_2(points, 0.5)

    points = [(0, 0), (1, 0), (0, 0)]
    assert not lic_2(points, 0)
    points = [(1, 0), (0, 0), (0, 1)]
    assert not lic_2(points,math.pi/2)

def test_lic_5() -> None:
    '''
    There exists at least one set of two consecutive data points,
    (X[i],Y[i]) and (X[j],Y[j]), such
    that X[j] - X[i] < 0. (where i = j-1)
    '''
    points = [(1, 0), (0, 0)]
    assert lic_5(points)
    points = [(2, 3), (3, 4), (2, 4)]
    assert lic_5(points)

    points = [(0, 0), (1, 0)]
    assert not lic_5(points)
    points = [(1, 2), (3, 4), (4, 5)]
    assert not lic_5(points)

def test_lic_1() -> None:
    '''
    There exists at least one set of three consecutive data points
    that cannot all be contained within or on a circle of radius RADIUS1.
    (0 ≤ RADIUS1)
    '''

    # Invalid radius
    points = [(0, 0), (0, 2),(1,1)]
    radius = -1
    assert not lic_1(points,radius)

    # Too small radius
    points = [(0, 0), (0, 2),(1,1)]
    radius = 0.5
    assert lic_1(points,radius)

    # Exact radius
    points = [(0, 0), (0, 2),(1,1)]
    radius = 1
    assert not lic_1(points,radius)

    # Larger radius
    points = [(0, 0), (0, 2),(1,1)]
    radius = 2
    assert not lic_1(points,radius)

    # Two overlapping sets, none uncontainable
    points = [(-1,2),(0, 0), (0, 2),(1,2)]
    radius = 1
    assert lic_1(points,radius)

    # Two overlapping sets, one uncontainable
    points = [(-1,1),(0, 0), (0, 2),(1,2)]
    radius = 1
    assert lic_1(points,radius)

    # Two overlapping sets, both containable
    points = [(-1,1),(0, 0), (0, 2),(1,1)]
    radius = 1
    assert not lic_1(points,radius)

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
    a_pts = 1
    b_pts = 1
    assert lic_8(points,radius,a_pts,b_pts)

    # Two overlapping sets, one uncontainable
    points = [(-1,2), (0, 0), (0, 0), (0, 2), (0, 2), (1,1)]
    a_pts = 1
    b_pts = 1
    assert lic_8(points,radius,a_pts,b_pts)

    # Two overlapping sets, both containable
    points = [(-1,1), (0, 0), (0, 0), (0, 2), (0, 2), (1,1)]
    a_pts = 1
    b_pts = 1
    assert not lic_8(points,radius,a_pts,b_pts)
