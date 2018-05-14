import algorithms as alg

def problem4(t0, N_A0, n, a, b, returnlist=False):
    """Uses Euler's method to graph the solution to a radioactive decay problem where dNA/dt = -NA/tauA and dNB/dt = NA/tauA - N

    Args:
        t0 (float): Start time
        tf (float): End time
        n (float): Number of points to sample at
        a (float): A constant such that dv/dt = a - bv
        b (float): A constant such that dv/dt = a - bv
        returnlist (bool) = Controls whether the function returns the list of points or not. Defaults to false

    Returns:
        solution (list): Points on the graph of the approximate solution as a list of tuples
    """
    print("Problem 3: ~Terminal Velocity~ dv/dt = a - bv")
    def vel(t, v):
        return a - b*v

    h = (tf-t0)/(n-1)
    print("Graph of approximate solution")
    print("Time step of %f seconds." % h)
    solution = alg.euler(t0, tf, n, 0, vel)
    print("Conclusion: Terminal velocity is about %f." % solution[n-1][1])
    if returnlist:
        return solution
