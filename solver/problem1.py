import algorithms as alg

def problem1(t0, tf, v0):
    """Uses Euler's method to graph velocity subject to Earth's gravity run as function of time, with 2, 5, and 10 sample points

    Args:
        t0 (float): Start time
        tf (float): End time
        v0 (float): Initial velocity
    """
    print("Problem 1: ~Gravity~ dv/dt = -g")
    def accel(t,v):
        return -9.8

    print("Approximate solutions:")
    h = (tf-t0)/2
    print("Time step of %f seconds." % h)
    print(alg.euler(t0, tf, 3,v0, accel))

    h = (tf-t0)/5
    print("Time step of %f seconds." % h)
    print(alg.euler(t0, tf, 6,v0, accel))

    h = (tf-t0)/10
    print("Time step of %f seconds." % h)
    print(alg.euler(t0, tf, 11,v0, accel))

    print("Conclusion: v = v0 - gt")
