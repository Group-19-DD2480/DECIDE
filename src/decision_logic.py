from lic import *
from parameters import PARAMETERS_T

def calculate_CMV(points: list[tuple[float, float]], parameters: PARAMETERS_T) -> list[bool]:
    """
    Calculate the Conditions Met Vector (CMV) based on the given points and parameters.

    This function iterates over all 15 Launch Interceptor Conditions (LICs) and sets 
    the corresponding element in the CMV to True if the LIC is met, and False otherwise.

    Parameters:
        points (list of tuples): A list of tuples representing points (X, Y).
        parameters (dict): A dictionary containing the parameters for the LICs.
        
    Returns:
        list of bool: The Conditions Met Vector (CMV) which is set to True if the LIC is met, and False otherwise.
    """

    CMV = [False] * 15

    CMV[0] = lic_0(points, parameters.length_1)
    CMV[1] = lic_1(points, parameters.radius_1)
    CMV[2] = lic_2(points, parameters.epsilon)
    CMV[3] = lic_3(points, parameters.area_1)
    CMV[4] = lic_4(points, parameters.q_pts, parameters.quads)
    CMV[5] = lic_5(points)
    CMV[6] = lic_6(points, parameters.n_pts, parameters.dist)
    CMV[7] = lic_7(points, parameters.k_pts, parameters.length_1)
    CMV[8] = lic_8(points, parameters.radius_1, parameters.a_pts, parameters.b_pts)
    CMV[9] = lic_9(points, parameters.c_pts, parameters.d_pts, parameters.epsilon)
    CMV[10] = lic_10(points, parameters.e_pts, parameters.f_pts, parameters.area_1)
    CMV[11] = lic_11(points, parameters.g_pts)
    CMV[12] = lic_12(points, parameters.k_pts, parameters.length_1, parameters.length_2)
    CMV[14] = lic_14(points, parameters.e_pts, parameters.f_pts, parameters.area_1, parameters.area_2)
    CMV[13] = lic_13(points, parameters.radius_1, parameters.radius_2, parameters.a_pts, parameters.b_pts)

    return CMV



def calculate_PUM(LCM: list[list[str]], CMV: list[bool]) -> list[list[bool]]:
    """
    The Preliminary Unlocking Matrix (PUM) is formed by using the Conditions Met Vector (CMV) in conjuction
    with the Logical Connector Matrix (LCM).

    Parameters:
        LCM (list[List[str]]): A matrix of bolean operations, ANDD, ORR or NOTUSED.
        CMV (list[bool]): CMV[i] is True if lic_i returns True.

    Returns:
        list[list[bool]]: A matrix where each element is the result 
      of applying the bolean operations specified in LCM to the corresponding elements in CMV.
    """
    ANDD, ORR, NOTUSED = "ANDD", "ORR", "NOTUSED"
    size = len(CMV)
    PUM = [[True] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            elif LCM[i][j] == NOTUSED:
                continue
            elif LCM[i][j] == ANDD:
                PUM[i][j] = CMV[i] and CMV[j]
            elif LCM[i][j] == ORR:
                PUM[i][j] = CMV[i] or CMV[j]
    return PUM


def Calculate_FUV(PUM, PUV):
    """
    The Final Unlocking Vector (FUV) is generated from the Preliminary Unlocking Matrix. The
    input PUV indicates whether the corresponding LIC is to be considered as a factor in signaling
    interceptor launch. FUV[i] should be set to true if PUV[i] is false (indicating that the associated
    LIC should not hold back launch) or if all elements in PUM row i are true.
    """
    pass


def Calculate_Launch(FUV: list[bool]) -> bool:
    """
    The final launch/no launch decision is based on the FUV. The decision to launch requires that all
    elements in the FUV be true, i.e. LAUNCH should be set to true if and only if FUV[i] is true for
    all i, 0 i 14. Forthe example, LAUNCH is false because FUV[0] is false.
    """
    pass
