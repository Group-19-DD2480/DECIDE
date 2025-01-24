import numpy as np


def lic_3(points: list[tuple[float, float]], area: float) -> bool:
    '''
    There exists at least one set of three consecutive data points that
    are the vertices of a triangle with area greater than AREA1.
    (0 <= AREA1)

    Parameters:
        points (list[tuple[float, float]]): List of 2D points [(x_1, y_1), (x_2, y_2), ...].
        area: Area that the triangle should be larger than

    Returns:
        bool: True if the area of a triangle of any three consecutive
              data points is strictly greater than the given area,
              false otherwise
    '''
    if area < 0:
        return False

    for set in zip(points, points[1:], points[2:]):
        set = np.array(set)
        p1 = set[0]
        p2 = set[1]
        p3 = set[2]
        area_of_triangle = (1/2) * abs(
                                       p1[0] * (p2[1] - p3[1]) +
                                       p2[0] * (p3[1] - p1[1]) +
                                       p3[0] * (p1[1] - p2[1])
                                       )
        if area_of_triangle > area:
            return True

    # No sets create a large enough triangle
    return False

def lic_5(points: list[tuple[float, float]]) -> bool:
    '''
    There exists at least one set of two consecutive data points,
    (X[i],Y[i]) and (X[j],Y[j]), such
    that X[j] - X[i] < 0. (where i = j-1)

    Parameters:
        points (list[tuple[float, float]]): List of 2D points [(x_1, y_1), (x_2, y_2), ...].

    Returns:
        bool: True if the x values of two consecutive data points are decreasing, False otherwise.
    '''
    for (x_i, _), (x_j, _) in zip(points, points[1:]):
        if x_j - x_i < 0:
            return True

    return False
