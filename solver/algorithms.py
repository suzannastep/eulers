"""
Suzanna Stephenson
May 9, 2018
Functions for euler, improved euler, and runge kutta algorithms to approximate solutions to differential equations
"""
import numpy as np
from matplotlib import pyplot as plt

def validinput(x0, xf, n):
    """Checks that the user input is valid.

    Args:
        x0 (float): Start value
        xf (float): End values
        n (int): Number of sample points

    Returns:
        False if x0 > xf or if
        True otherwise
    """
    isvalid == True
    if x0 > xf:
        isvalid = False
    if int(n) != n:
        isvalid = False
    if isvalid == False:
        print(Please recheck your input)
    return isvalid

def graphsol(xvals, yvals): # pragma: no cover
    """Graphs the aproximate solution to a differential equation

    Args:
        xvals (list): A list of x coordinates of points
        yvals (list): A corresponding list of y coordinates of points in the solution
    """
    plt.plot(xvals,yvals)
    plt.xlim(min(0, min(xvals)-1), max(0, max(xvals)+1))
    plt.ylim(min(0, min(yvals)-1), max(0, max(yvals)+1))
    plt.show()

def euleriteration(xi, yi, h, f):
    """Performs one iteration of Euler's method.

    Args:
        xi (float): The previous x value
        yi (float): The previous y value
        h (float): The step size
        f (function): The derivative of y at That is, y' = f(x,y). f must be a defined before as function of x and y, in that order

    Returns:
        The next y value as a float
    """
    return yi + h * f(xi, yi)

def euler(x0, xf, n, y0, f, graph=True):
    """Uses Euler's method to calculate the approximate solution of a differential equation

    Args:
        x0 (float): The left endpoint of the domain
        xf (float): The right endpoint of the domain
        n (int): The number of x-values to aproximate the solution at. Determines the step size
        y0 (float): The the initial condition
        f (function): The derivative of y at That is, y' = f(x,y). f must be a defined before as function of x and y, in that order
        graph (bool): Whether the user wants to graph the aproximate solution using matplotlib

    Returns:
        pointlist (list): A list of ordered pairs on the approximation of the solution curve
    """
    if validinput(x0, xf, n) == True:
        h = (xf - x0)/(n-1)
        yvals = [y0]
        xvals = np.linspace(x0, xf, n)
        for i in np.arange(n-1):
            yvals.append(euleriteration(xvals[i], yvals[i], h, f)) #append y_{i+1}
        if graph:
            graphsol(xvals, yvals)
        pointlist = [(xvals[i], yvals[i]) for i in np.arange(n)]
        return pointlist

def improvedeuleriteration(xi, yi, h, f):
    """Performs one iteration of Improved Euler's method.

    Args:
        xi (float): The previous x value
        yi (float): The previous y value
        h (float): The step size
        f (function): The derivative of y at That is, y' = f(x,y). f must be a defined before as function of x and y, in that order

    Returns:
        The next y value as a float
    """
    m1 = f(xi, yi)
    m2 = f(xi + h, yi + h * m1)
    return yi + h /2 * (m1 + m2)

def improvedeuler(x0, xf, n, y0, f, graph=True):
    """Uses Improved Euler's method to calculate the approximate solution of a differential equation

    Args:
        x0 (float): The left endpoint of the domain
        xf (float): The right endpoint of the domain
        n (int): The number of x-values to aproximate the solution at. Determines the step size
        y0 (float): The the initial condition
        f (function): The derivative of y at That is, y' = f(x,y). f must be a defined before as function of x and y, in that order
        graph (bool): Whether the user wants to graph the aproximate solution using matplotlib

    Returns:
        pointlist (list): A list of ordered pairs on the approximation of the solution curve

    """
    if validinput(x0, xf, n) == True:
        h = (xf - x0)/(n-1)
        yvals = [y0]
        xvals = np.linspace(x0, xf, n)
        for i in np.arange(n-1):
            yvals.append(improvedeuleriteration(xvals[i], yvals[i], h, f)) #append y_{i+1}
        if graph:
            graphsol(xvals, yvals)
        pointlist = [(xvals[i], yvals[i]) for i in np.arange(n)]
        return pointlist

def rungekuttaiteration(xi, yi, h, f):
    """Performs one iteration of the Runge Kutta algorithm.

    Args:
        xi (float): The previous x value
        yi (float): The previous y value
        h (float): The step size
        f (function): The derivative of y at That is, y' = f(x,y). f must be a defined before as function of x and y, in that order

    Returns:
        The next y value as a float
    """

    k1 = f(xi, yi)
    k2 = f(xi + (h/2), yi + h*(k1/2))
    k3 = f(xi + h/2, yi + h*k2/2)
    k4 = f(xi + h, yi + h*k3)
    return yi + h * (k1 + 2*k2 + 2*k3 + k4) /6

def rungekutta(x0, xf, n, y0, f, graph=True):
    """Uses the Runge Kutta algorithm to calculate the approximate solution of a differential equation

    Args:
        x0 (float): The left endpoint of the domain
        xf (float): The right endpoint of the domain
        n (int): The number of x-values to aproximate the solution at. Determines the step size
        y0 (float): The the initial condition
        f (function): The derivative of y at That is, y' = f(x,y). f must be a defined before as function of x and y, in that order
        graph (bool): Whether the user wants to graph the aproximate solution using matplotlib

    Returns:
        pointlist (list): A list of ordered pairs on the approximation of the solution curve
    """
    if validinput(x0, xf, n) == True:
        h = (xf - x0)/(n-1)
        yvals = [y0]
        xvals = np.linspace(x0, xf, n)
        for i in np.arange(n-1):
            yvals.append(rungekuttaiteration(xvals[i], yvals[i], h, f)) #append y_{i+1}
        if graph:
            graphsol(xvals, yvals)
        pointlist = [(xvals[i], yvals[i]) for i in np.arange(n)]
        return pointlist
