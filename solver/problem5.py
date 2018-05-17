import algorithms as alg
import numpy as np

def problem5(t0, tf, NA0, NB0, tau, n, returnlist=False):
    """Uses Euler's method to model the solution to a radioactive decay problem where dNA/dt = NB/tau - NA/tau and dNB/dt = NA/tau - NB/tau.

    Args:
        t0 (float): Start time
        tf (float): End time
        NA0 (int): Initial number of NA nuclei
        NB0 (int): Initial number of NB nuclei
        tau (float): Decay time constant
        n (float): Number of points to sample at
        returnlist (bool) = Controls whether the function returns the list of points or not. Defaults to false

    Returns:
        solution (list): Points on the graph of the approximate solution. Each element in the list has the form (t, array([NA, NB]))

    In the graph, NA is green and NB is blue
    """
    print("Problem 5: ~Radioactive Decay~ dNA/dt = NB/tau - NA/tau & dNB/dt = NA/tau - NB/tau.")
    N0 = np.array([NA0, NB0])
    A = np.array([[-1/tau, 1/tau],[1/tau, -1/tau]])
    def dN_dt(t, N):
        return A @ N
    h = (tf-t0)/(n-1)
    print("Time step of %f seconds." % h)
    solution = alg.euler(t0, tf, n, N0, dN_dt)
    if returnlist:
        return solution
