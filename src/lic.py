

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
