import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from decision_logic import *
from parameters import PARAMETERS_T
from lic import *

def test_cmv() -> None:
    """
    Calculate the Conditions Met Vector (CMV) based on the given points and parameters.

    This function iterates over all 15 Launch Interceptor Conditions (LICs) and sets 
    the corresponding element in the CMV to True if the LIC is met, and False otherwise.
    """

    # Test if CMV[i] values change correctly based on the LICs
    points = [(0, 0), (0, 2), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0),(2, 2), (5, 2), (2, 5),(3, 3), (-3, 3), (-3, -3), (3, -3),
              (6, 6), (6, 8), (7, 6), (-1,2)]
    test_parameters = PARAMETERS_T(
            length_1=1,
            radius_1=0.5,
            epsilon=0.5,
            area_1=1.0,
            q_pts=0,
            quads=0,
            n_pts=3,
            dist=0,
            k_pts=0,
            a_pts=1,
            b_pts=1,
            c_pts=1,
            d_pts=1,
            e_pts=1,
            f_pts=1,
            g_pts=1,
            length_2=0,
            radius_2=0,
            area_2=0
        )
    
    CMV = calculate_CMV(points, test_parameters)
    assert CMV[0] == lic_0(points, test_parameters.length_1)
    assert CMV[1] == lic_1(points, test_parameters.radius_1)
    assert CMV[2] == lic_2(points, test_parameters.epsilon)
    assert CMV[3] == lic_3(points, test_parameters.area_1)
    assert CMV[4] == lic_4(points, test_parameters.q_pts, test_parameters.quads)
    assert CMV[5] == lic_5(points)
    assert CMV[6] == lic_6(points, test_parameters.n_pts, test_parameters.dist)
    assert CMV[7] == lic_7(points, test_parameters.k_pts, test_parameters.length_1)
    assert CMV[8] == lic_8(points, test_parameters.radius_1, test_parameters.a_pts, test_parameters.b_pts)
    assert CMV[9] == lic_9(points, test_parameters.c_pts, test_parameters.d_pts, test_parameters.epsilon)
    assert CMV[10] == lic_10(points, test_parameters.e_pts, test_parameters.f_pts, test_parameters.area_1)
    assert CMV[11] == lic_11(points, test_parameters.g_pts)
    assert CMV[12] == lic_12(points, test_parameters.k_pts, test_parameters.length_1, test_parameters.length_2)
    assert CMV[13] == lic_13(points, test_parameters.radius_1, test_parameters.radius_2, test_parameters.a_pts, test_parameters.b_pts)
    assert CMV[14] == lic_14(points, test_parameters.e_pts, test_parameters.f_pts, test_parameters.area_1, test_parameters.area_2)

