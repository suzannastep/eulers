import solver.algorithms as alg

def problem1(t0, tf, v0):
    """Uses Euler's method to graph velocity subject to Earth's gravity run as function of time, with 2, 5, and 10 sample points

    Args:
        t0 (float): Start time
        tf (float): End time
        v0 (float): Initial velocity

    Returns:
        twopoints (List): Two points on the solution curve.
        fivepoints (List): Five points on the solution curve.
        tenpoints (List): Ten points on the solution curve.
    """
    print("Problem 1: ~Gravity~ dv/dt = -g")
    def accel(t,v):
        return -9.8

    print("Approximate solutions:")
    h = (tf-t0)/2
    twopoints = alg.euler(t0, tf, 3,v0, accel)
    print("Time step of %f seconds." % h)
    print(twopoints)

    h = (tf-t0)/5
    fivepoints = alg.euler(t0, tf, 6, v0, accel)
    print("Time step of %f seconds." % h)
    print(fivepoints)

    h = (tf-t0)/10
    tenpoints = alg.euler(t0, tf, 11,v0, accel)
    print("Time step of %f seconds." % h)
    print(tenpoints)

    print("Conclusion: v = v0 - g * t")

    return twopoints, fivepoints, tenpoints
