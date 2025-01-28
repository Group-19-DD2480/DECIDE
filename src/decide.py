import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from decision_logic import calculate_CMV, calculate_PUM, calculate_FUV, calculate_launch


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
    PUM = calculate_PUM(CMV, LCM)
    FUV = calculate_FUV(PUM, PUV)
    is_launch = calculate_launch(FUV)

    # Print the result
    print("YES") if is_launch else print("NO")
    