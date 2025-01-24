import numpy as np


def lic_0(points: list[tuple[float, float]], length_1: float) -> bool:
    """
    Determines if there exists at least one set of two consecutive data points
    whose distance is greater than LENGTH1.

    Parameters:
        points (List[Tuple[float, float]]): List of 2D points [(x1, y1), (x2, y2), ...].
        length_1 (float): Threshold distance (must be non-negative).

    Returns:
        bool: True if any consecutive points are farther apart than LENGTH1, else False.
    """
    if len(points) < 2:
        return False
    for i in range(len(points) - 1):
        if np.linalg.norm(np.array(points[i]) - np.array(points[i + 1])) > length_1:
            return True
    return False
