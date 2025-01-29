import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from decision_logic import calculate_CMV, calculate_PUM, Calculate_FUV, Calculate_Launch


def decide(points: list[tuple[float, float]], parameters, LCM: list[list[str]], PUV: list[bool]) -> None:
    """
    The main DECIDE function that determine whether to launch an interceptor.

    Parameters:
        points (list[tuple[float, float]]): List of planar points (x, y).
        parameters (object): Contains parameters for the LICs.
        LCM (list[list[str]]): Logical Connector Matrix.
        PUV (list[bool]): Preliminary Unlocking Vector.
       
    """
    CMV = calculate_CMV(points, parameters)
    PUM = calculate_PUM(LCM, CMV)
    FUV = Calculate_FUV(PUM, PUV)
    is_launch = Calculate_Launch(FUV)

    # Print the result
    print("YES") if is_launch else print("NO")
    
