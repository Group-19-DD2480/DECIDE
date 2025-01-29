import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from decision_logic import calculate_CMV, calculate_PUM, Calculate_FUV, Calculate_Launch
from parameters import PARAMETERS_T

points: list[tuple[float, float]] = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
num_points: int = len(points)
LCM: list[list[str]] = [
    ["ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",],
    ["ANDD", "ANDD", "ORR", "ORR", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",],
    ["ORR", "ORR", "ANDD", "ANDD", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",],
    ["ANDD", "ORR", "ANDD", "ANDD", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",],
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",],
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
    ["NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED",], 
]
PUM: list[list[bool]] 
CMV: list[bool] 
PUV: list[bool] = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,]
FUV = list[bool] 
launch: bool 
parameters:PARAMETERS_T = PARAMETERS_T()


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
    
if __name__ == "__main__":
    decide(points, parameters, LCM, PUV)

