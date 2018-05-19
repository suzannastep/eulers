import solver.algorithms as alg

def problem6(t0, tf, N0, n, a, b, returnlist=False):
    """Uses Euler's method to graph the size of a population based on the model dN/dt = aN - bN^2.

    Args:
        t0 (float): Start time
        tf (float): End time
        N (int): initial population
        n (float): Number of points to sample at
        a (float): A constant related to the birth of new members of the population
        b (float): A constant related to the deaths of members of the population
        returnlist (bool) = Controls whether the function returns the list of points or not. Defaults to false

    Returns:
        solution (list): Points on the graph of the approximate solution as a list of tuples of returnlist is set to true
    """
    print("Problem 6: ~Population Modeling~ dN/dt = aN - bN^2")
    def deltapop(t, N):
        return a*N - b*N**2

    h = (tf-t0)/(n-1)
    print("Graph of approximate solution")
    print("Time step of %f seconds." % h)
    solution = alg.euler(t0, tf, n, N0, deltapop)
    print("Conclusion: Population size will approach %f." % solution[n-1][1])
    if returnlist:
        return solution
