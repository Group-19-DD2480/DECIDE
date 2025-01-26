import numpy as np
import math


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


def area_of_triangle(set: np.ndarray):
    p1 = set[0]
    p2 = set[1]
    p3 = set[2]
    area_of_triangle = (1/2) * abs(
                                   p1[0] * (p2[1] - p3[1]) +
                                   p2[0] * (p3[1] - p1[1]) +
                                   p3[0] * (p1[1] - p2[1])
                                   )
    return area_of_triangle


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
        if area_of_triangle(set) > area:
            return True

    # No sets create a large enough triangle
    return False

def lic_4(points: list[tuple[float, float]], q_pts: int, quads: int) -> bool:
    """
    There exists at least one set of Q_PTS consecutive data points that lie in more than QUADS
    quadrants. Where there is ambiguity as to which quadrant contains a given point, priority
    of decision will be by quadrant number, i.e., I, II, III, IV. For example, the data point (0,0)
    is in quadrant I, the point (-1,0) is in quadrant II, the point (0,-1) is in quadrant III, the point
    (0,1) is in quadrant I and the point (1,0) is in quadrant I.
    (2 <= Q_PTS <= NUMPOINTS),(1 <= QUADS <= 3)

    Parameters:
        points (list[tuple[float, float]]): List of 2D points [(x_1, y_1), (x_2, y_2), ...].
        q_pts (int): Number of points to consider.
        quads (int): Number of quadrants to consider.

    Returns:
        bool: True if the LIC 4 condition is met, False, otherwise.
    """
    if q_pts < 2 or q_pts > len(points) or quads < 1 or quads > 3:
        return False
    
    def get_quadrant(point):
        """Determine the quadrant of a given point."""
        x, y = point
        if x >= 0 and y >= 0:
            return 1  # Quadrant I
        elif x <= 0 and y >= 0:
            return 2  # Quadrant II
        elif x <= 0 and y <= 0:
            return 3  # Quadrant III
        elif x >= 0 and y <= 0:
            return 4
        else:
            return None
    
    for i in range(len(points) - q_pts + 1):
        quadrants = set()
        for j in range(i, i + q_pts):
            quadrant = get_quadrant(points[j])
            if quadrant is not None:
                quadrants.add(quadrant)
            if len(quadrants) > quads:
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


def lic_6(points: list[tuple[float, float]], n_pts: int, dist: float):
    """
    There exists at least one set of N PTS consecutive data points such that at least one of the
    points lies a distance greater than DIST from the line joining the first and last of these N PTS
    points. If the first and last points of these N PTS are identical, then the calculated distance
    to compare with DIST will be the distance from the coincident point to all other points of
    the N PTS consecutive points. The condition is not met when NUMPOINTS < 3.
    (3 ≤ N PTS ≤ NUMPOINTS), (0 ≤ DIST)

    Parameters:
        points (list[tuple[float, float]]): A list of 2D points [(x1, y1), (x2, y2), ...].
        n_pts (int): Number of consecutive points.
        dist (float): Minimum distance from line.
    
    Returns:
        bool: True if there exists a set of n_pts points such that there exists
            a point at a distance greater than list from the line connecting the first
            and last point in the set, if the first and last point are equal then the distance
            is from the coincident point instead. False otherwise.
    """
    def distance_to_line(first: tuple[float, float], last: tuple[float, float], point: tuple[float, float]):
        """
        Calculated the distance of point to the line defined by first and last.
        If first and last are equal then the distance is calculated from the coincident point instead.

        Parameters:
            first (tuple[float, float]): The first point that defines the line.
            last (tuple[float, float]): The second point that defines the line.
            point (tuple[float, float]): The point that the distance is calculated to.

        Returns:
            float: the distance from point to the line defined by first and last,
                if first and last are equal the distance is calculated from the coincident point.
        """
        x1, y1 = first
        x2, y2 = last
        x, y = point

        #If first and last are equal the distance is calculated from the coincident point.
        if first == last:
            return math.sqrt((x - x1)**2 + (y - y1)**2)
        
        #Line equation Ax + By + C = 0
        A = y2 - y1
        B = x1 - x2
        C = x2 * y1 - x1 * y2

        return abs(A * x + B * y + C) / math.sqrt(A**2 + B**2)


    if len(points) < 3:
        return False
    
    for i in range(len(points) - n_pts + 1):
        subset = points[i:i + n_pts]
        first, last = subset[0], subset[-1]
        for point in subset:
            if distance_to_line(first, last, point) > dist:
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

def lic_8(points: list[tuple[float, float]], radius: float, a_pts: int, b_pts: int) -> bool:
    '''
     There exists at least one set of three data points separated by exactly A PTS and B PTS
    consecutive intervening points, respectively, that cannot be contained within or on a circle of
    radius RADIUS1. The condition is not met when NUMPOINTS < 5.
    1 ≤ A PTS, 1 ≤ B PTS
    A PTS+B PTS ≤ (NUMPOINTS−3)

    '''
    
    # Tolerance for comparing exact radius match
    REL_TOL = 1+1e-09

    # Invalid parameters
    if radius < 0 or a_pts < 1 or b_pts <1 or len(points) < a_pts + b_pts + 3:
        return False

    for set in zip(points, points[1+a_pts:],points[2+a_pts+b_pts:]):
        # Calculate sides of the triangle formed by the points
        set = np.array(set)
        a = np.linalg.norm(set[0] - set[1])
        b = np.linalg.norm(set[0] - set[2])
        c = np.linalg.norm(set[1] - set[2])

        # Calculate the circumcircle radius
        cc_radius = a * b * c / np.sqrt((a+b+c)*(b+c-a)*(a+c-b)*(a+b-c))
        # Return True if the circumcircle radius is larger and thus uncontainable by radius
        if cc_radius  > radius * REL_TOL:
            return True

    # If all sets are containable
    return False

def lic_9(points: list[tuple[float, float]], c_pts: int, d_pts: int, epsilon: float) -> bool:
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

    Parameters:
        points (list[tuple[float, float]]): List of 2D points [(x_1, y_1), (x_2, y_2), ...].
        c_pts (int): Number of points between the first and second point.
        d_pts (int): Number of points between the second and third point.
        epsilon (float): A float value representing the deviation from PI

    Returns:
        bool: True if the LIC 9 condition is met, False, otherwise
    """
    if c_pts < 1 or d_pts < 1 or c_pts + d_pts > (len(points) - 3) or len(points) < 5:
        return False

    for i in range(len(points) - c_pts - d_pts - 2):
        p1 = points[i]
        p2 = points[i + c_pts + 1]
        p3 = points[i + c_pts + d_pts + 2]

        if p1 == p2 or p2 == p3 or p1 == p3:
            continue

        angle = calculate_angle(p1, p2, p3)
        if angle is not None and (angle < math.pi - epsilon or angle > math.pi + epsilon):
            return True

    return False

def lic_10(points: list[tuple[float, float]], e_pts: int, f_pts: int, area1) -> bool:
    """
    There exists at least one set of three data points separated by exactly E PTS and F PTS con-
    secutive intervening points, respectively, that are the vertices of a triangle with area greater
    than AREA1. The condition is not met when NUMPOINTS < 5.

    1 ≤ E PTS, 1 ≤ F PTS
    E PTS + F PTS ≤ NUMPOINTS − 3

    Parameters:
        points (list[tuple[float, float]]): A list of 2D points [(x1, y1), (x2, y2), ...].
        e_pts: Number of consecutive points that separates the first and second point in the triangle
        f_pts: Number of consecutive points that separates the second and third point in the triangle
        area1: Area that the triangle should be strictly greater than

    Returns:
        bool: True if the area of a triangle of any three data points separated by e_pts and f_pts,
              is strictly greater than the given area, false otherwise
    """
    if len(points) < 5:
        return False

    if 1 > e_pts or 1 > f_pts:
        return False

    if e_pts + f_pts > len(points) - 3:
        return False

    for set in zip(points, points[1+e_pts:], points[2+e_pts + f_pts:]):
        if area_of_triangle(set) > area1:
            return True

    return False

def lic_11():
    """
    There exists at least one set of two data points, (X[i],Y[i]) and (X[j],Y[j]), separated by
    exactly G PTS consecutive intervening points, such that X[j] - X[i] < 0. (where i < j ) The
    condition is not met when NUMPOINTS < 3.

    1 ≤ G PTS ≤ NUMPOINTS − 2
    """


def lic_12():
    """
    There exists at least one set of two data points, separated by exactly K PTS consecutive
    intervening points, which are a distance greater than the length, LENGTH1, apart. In addi-
    tion, there exists at least one set of two data points (which can be the same or different from
    the two data points just mentioned), separated by exactly K PTS consecutive intervening
    points, that are a distance less than the length, LENGTH2, apart. Both parts must be true
    for the LIC to be true. The condition is not met when NUMPOINTS < 3.

    0 ≤ LENGTH2
    """

def lic_13(points: list[tuple[float, float]], radius1: float, radius2: float, a_pts: int, b_pts: int) -> bool:
    '''
    There exists at least one set of three data points, separated by exactly A PTS and B PTS
    consecutive intervening points, respectively, that cannot be contained within or on a circle of
    radius RADIUS1. In addition, there exists at least one set of three data points (which can be
    the same or different from the three data points just mentioned) separated by exactly A PTS
    and B PTS consecutive intervening points, respectively, that can be contained in or on a
    circle of radius RADIUS2. Both parts must be true for the LIC to be true. The condition is
    not met when NUMPOINTS < 5.
    0 ≤ RADIUS2

    '''
    
    # Tolerance for comparing exact radius match
    REL_TOL = 1+1e-09

    # Invalid parameters
    if radius1 < 0 or radius2 < 0 or a_pts < 1 or b_pts <1 or len(points) < a_pts + b_pts + 3:
        return False
    
    radius1_uncont = False
    radius2_cont = False

    for set in zip(points, points[1+a_pts:],points[2+a_pts+b_pts:]):
        # Calculate sides of the triangle formed by the points
        set = np.array(set)
        a = np.linalg.norm(set[0] - set[1])
        b = np.linalg.norm(set[0] - set[2])
        c = np.linalg.norm(set[1] - set[2])

        # Calculate the circumcircle radius
        cc_radius = a * b * c / np.sqrt((a+b+c)*(b+c-a)*(a+c-b)*(a+b-c))

        # Compare the circumricle radius to radius1 and radius2
        if cc_radius  > radius1 * REL_TOL:
            radius1_uncont = True
        if cc_radius  <= radius2 * REL_TOL:
            radius2_cont = True
    # Return True only if both radii conditions are satisfied
    return radius1_uncont and radius2_cont

def lic_14():
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
