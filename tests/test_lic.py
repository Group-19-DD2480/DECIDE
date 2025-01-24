from src.lic import *


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
