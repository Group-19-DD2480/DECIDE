def Calculate_CMV():
    """
     The Conditions Met Vector (CMV) is set according to the results of the LICs, i.e.
     the global array element CMV[i] should be set to true if and only if the ith LIC is met.
    """
    pass


def Calculate_PUM(CMV, LCM):
    """
    Te Preliminary Unlocking Matrix (PUM) is formed by using the Conditions Met Vector (CMV) in conjuction 
    with the Logical Connector Matrix (LCM).
    """
    pass


def Calculate_FUV(PUM, PUV):
    """
    The Final Unlocking Vector (FUV) is generated from the Preliminary Unlocking Matrix. The
    input PUV indicates whether the corresponding LIC is to be considered as a factor in signaling
    interceptor launch. FUV[i] should be set to true if PUV[i] is false (indicating that the associated
    LIC should not hold back launch) or if all elements in PUM row i are true.
    """
    pass


def Calculate_Launch(FUV):
    """
    The final launch/no launch decision is based on the FUV. The decision to launch requires that all
    elements in the FUV be true, i.e. LAUNCH should be set to true if and only if FUV[i] is true for
    all i, 0 i 14. Forthe example, LAUNCH is false because FUV[0] is false.
    """
    pass
