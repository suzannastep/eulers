import algorithms as alg

def problem2(t0, tf, x0, v):
    """Uses Euler's method to graph position as function of time, with 2, 5, and 10 sample points

    Args:
        t0 (float): Start time
        tf (float): End time
        x0 (float): Initial position
        v (float): Velocity (assumed to be a constant)
    """
    print("Problem 2: ~Position~ dx/dt = -v")
    def vel(t, x):
        return v

    print("Approximate solutions:")
    h = (tf-t0)/2
    print("Time step of %f seconds." % h)
    print(alg.euler(t0, tf, 3, x0, vel))

    h = (tf-t0)/5
    print("Time step of %f seconds." % h)
    print(alg.euler(t0, tf, 6, x0, vel))

    h = (tf-t0)/10
    print("Time step of %f seconds." % h)
    print(alg.euler(t0, tf, 11, x0, vel))

    print("Conclusion: x = x0 + vt")
