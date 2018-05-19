import solver.algorithms as alg

def problem2(t0, tf, x0, v):
    """Uses Euler's method to graph position as function of time, with 2, 5, and 10 sample points

    Args:
        t0 (float): Start time
        tf (float): End time
        x0 (float): Initial position
        v (float): Velocity (assumed to be a constant)

    Returns:
        twopoints (List): Two points on the solution curve.
        fivepoints (List): Five points on the solution curve.
        tenpoints (List): Ten points on the solution curve.
    """
    print("Problem 2: ~Position~ dx/dt = -v")
    def vel(t, x):
        return v

    print("Approximate solutions:")
    h = (tf-t0)/2
    print("Time step of %f seconds." % h)
    threepoints = alg.euler(t0, tf, 3, x0, vel)
    print(threepoints)

    h = (tf-t0)/5
    print("Time step of %f seconds." % h)
    sixpoints = alg.euler(t0, tf, 6, x0, vel)
    print(sixpoints)

    h = (tf-t0)/10
    print("Time step of %f seconds." % h)
    elevenpoints = alg.euler(t0, tf, 11, x0, vel)
    print(elevenpoints)

    print("Conclusion: x = x0 + v * t")

    return threepoints, sixpoints, elevenpoints
