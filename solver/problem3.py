import solver.algorithms as alg

def problem3(t0, tf, n, a, b, returnlist=False):
    """Uses Euler's method to graph velocity of an object subject to friction and approximate terminal velocity
    Assumes that the the objects starts at the origin.

    Args:
        t0 (float): Start time
        tf (float): End time
        n (float): Number of points to sample at
        a (float): A constant such that dv/dt = a - bv
        b (float): A constant such that dv/dt = a - bv
        returnlist (bool) = Controls whether the function returns the list of points or not. Defaults to false

    Returns:
        solution (list): Points on the graph of the approximate solution as a list of tuples
        terminalvelocity (float): An approximation of the terminal velocity
    """
    print("Problem 3: ~Terminal Velocity~ dv/dt = a - bv")
    def vel(t, v):
        return a - b*v

    h = (tf-t0)/(n-1)
    print("Graph of approximate solution")
    print("Time step of %f seconds." % h)
    solution = alg.euler(t0, tf, n, 0, vel)
    terminalvelocity = solution[-1][1]
    print("Conclusion: Terminal velocity is about %f." % terminalvelocity)
    if returnlist:
        return solution, terminalvelocity
    else:
        return terminalvelocity
