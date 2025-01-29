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
    points = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    test_parameters = PARAMETERS_T(
            length_1=2,
            radius_1=0,
            epsilon=0.5,
            area_1=0,
            q_pts=0,
            quads=0,
            n_pts=3,
            dist=0,
            k_pts=0,
            a_pts=0,
            b_pts=0,
            c_pts=0,
            d_pts=0,
            e_pts=0,
            f_pts=0,
            g_pts=0,
            length_2=0,
            radius_2=0,
            area_2=0
        )
    
    CMV = calculate_CMV(points, test_parameters)
    assert CMV[0] == lic_0(points, test_parameters.length_1)
    assert CMV[3] == lic_2(points, test_parameters.epsilon)

