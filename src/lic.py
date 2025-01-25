import numpy as np
import math
import numpy as np


def lic_1(points: list[tuple[float, float]], radius: float) -> bool:
    """
    There exists at least one set of three consecutive data points
    that cannot all be contained within or on a circle of radius RADIUS1.
    (0 ≤ RADIUS1)

    """

    # Tolerance for comparing exact radius match
    REL_TOL = 1 + 1e-09

    if radius < 0:
        return False

    for set in zip(points, points[1:], points[2:]):
        # Calculate sides of the triangle formed by the points
        set = np.array(set)
        a = np.linalg.norm(set[0] - set[1])
        b = np.linalg.norm(set[0] - set[2])
        c = np.linalg.norm(set[1] - set[2])

        # Calculate the circumcircle radius
        cc_radius = (
            a * b * c / np.sqrt((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c))
        )

        # Return True if the circumcircle radius is larger and thus uncontainable by radius
        if cc_radius > radius * REL_TOL:
            return True

    # If all sets are containable
    return False


def lic_2(points: list[tuple[float, float]], epsilon: float) -> bool:
    """
    There exists at least one set of three consecutive data points which form an angle such that:
    angle < (PI - EPSILON)
    or
    angle > (PI + EPSILON)
    The second of the three consecutive points is always the vertex of the angle. If either the first
    point or the last point (or both) coincides with the vertex, the angle is undefined and the LIC
    is not satisfied by those three points.
    (0 <= EPSILON < PI)

    Parameters:
        points (list[tuple[float, float]]): List of 2D points [(x_1, y_1), (x_2, y_2), ...].
        epsilon (float): A float value representing the deviation from PI

    Returns:
        bool: True if the LIC 2 condition is met, False, otherwise.
    """

    def calculate_angle(p1, p2, p3):
        """
        Calculate the angle formed by three points p1, p2 (vertex), and p3.

        Parameters:
            p1 (tuple[float, float]): First point (x, y)
            p2 (tuple[float, float]): Second point (x, y)
            p3 (tuple[float, float]): Third point (x, y)

        Returns:
            float: The angle in radians formed by the three

        """
        v1 = (p1[0] - p2[0], p1[1] - p2[1])
        v2 = (p3[0] - p2[0], p3[1] - p2[1])
        dot_product = v1[0] * v2[0] + v1[1] * v2[1]

        mag_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
        mag_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)

        # Magnitude is 0, the angle is undefined
        if mag_v1 == 0 or mag_v2 == 0:
            return None

        cos_theta = dot_product / (mag_v1 * mag_v2)

        # Ensure cos_theta is within [-1, 1]
        cos_theta = max(min(cos_theta, 1), -1)

        return math.acos(cos_theta)

    if epsilon < 0 or epsilon >= math.pi:
        return False

    for i in range(len(points) - 2):
        p1 = points[i]
        p2 = points[i + 1]
        p3 = points[i + 2]

        if p1 == p2 or p2 == p3 or p1 == p3:
            continue

        angle = calculate_angle(p1, p2, p3)
        if angle is not None and (
            angle < math.pi - epsilon or angle > math.pi + epsilon
        ):
            return True
    return False


def lic_5(points: list[tuple[float, float]]) -> bool:
    """
    There exists at least one set of two consecutive data points,
    (X[i],Y[i]) and (X[j],Y[j]), such
    that X[j] - X[i] < 0. (where i = j-1)

    Parameters:
        points (list[tuple[float, float]]): List of 2D points [(x_1, y_1), (x_2, y_2), ...].

    Returns:
        bool: True if the x values of two consecutive data points are decreasing, False otherwise.
    """
    for (x_i, _), (x_j, _) in zip(points, points[1:]):
        if x_j - x_i < 0:
            return True
    return False

def lic_7(points: list[tuple[float, float]], k_pts: int, length_1: float) -> bool:
    """
    Determines if there exists at least one set of two data points separated by exactly
    k_pts consecutive intervening points that are a euclidean_dist greater than length_1 apart.

    Parameters:
        points (list[tuple[float, float]]): A list of 2D points [(x1, y1), (x2, y2), ...].
        k_pts (int): Number of consecutive intervening points between the two points.
        length_1 (float): Threshold euclidean_dist.

    Returns:
        bool: True if the condition is met, False otherwise.
    """
    NUMPOINTS = len(points)

    # Condition not met if NUMPOINTS < 3 or invalid k_pts
    if NUMPOINTS < 3 or k_pts < 1 or k_pts > NUMPOINTS - 2:
        return False

    for i in range(NUMPOINTS - k_pts - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + k_pts + 1]  # Separated by k_pts indexing
        euclidean_dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if euclidean_dist > length_1:
            return True
    return False
