import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from decision_logic import calculate_PUM

"""
The Preliminary Unlocking Matrix (PUM) is formed by using the Conditions Met Vector (CMV) in conjuction 
with the Logical Connector Matrix (LCM).
"""
ANDD, ORR, NOTUSED = "ANDD", "ORR", "NOTUSED"
def test_calculate_PUM_NOTUSED() -> None:
    LCM = [
        [NOTUSED, NOTUSED, NOTUSED, NOTUSED],
        [NOTUSED, NOTUSED, NOTUSED, NOTUSED],
        [NOTUSED, NOTUSED, NOTUSED, NOTUSED],
        [NOTUSED, NOTUSED, NOTUSED, NOTUSED]]
    CMV = [False, False, False, False]
    assert calculate_PUM(LCM, CMV) == [
        [True, True, True, True], 
        [True, True, True, True], 
        [True, True, True, True], 
        [True, True, True, True]]

def test_calculate_PUM_ORR() -> None:
    LCM = [
        [ORR, ORR, ORR, ORR],
        [ORR, ORR, ORR, ORR],
        [ORR, ORR, ORR, ORR],
        [ORR, ORR, ORR, ORR]]
    CMV = [True, False, True, False]
    assert calculate_PUM(LCM, CMV) == [
        [True, True, True, True],
        [True, True, True, False],
        [True, True, True, True],
        [True, False, True, True]]
    
def test_calculate_PUM_ANDD() -> None:
    LCM = [
        [ANDD, ANDD, ANDD, ANDD],
        [ANDD, ANDD, ANDD, ANDD],
        [ANDD, ANDD, ANDD, ANDD],
        [ANDD, ANDD, ANDD, ANDD]]
    CMV = [True, False, True, False]
    assert calculate_PUM(LCM, CMV) == [
        [True, False, True, False],
        [False, True, False, False],
        [True, False, True, False],
        [False, False, False, True]]

def test_calculate_PUM_diagonal() -> None:
    LCM = [
        [ANDD, ANDD, ANDD, ANDD],
        [ANDD, ANDD, ANDD, ANDD],
        [ANDD, ANDD, ANDD, ANDD],
        [ANDD, ANDD, ANDD, ANDD]]
    CMV = [False, False, False, False]
    assert calculate_PUM(LCM, CMV) == [
        [True, False, False, False],
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True]]
