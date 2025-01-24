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
