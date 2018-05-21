import numpy as np

def test_validinput():
    from solver.algorithms import validinput

    assert validinput(5, 0, 12) == False
    assert validinput(0, 5, 1.2) == False
    assert validinput(0, 5, 4) == True

def test_euleriteration():
    from solver.algorithms import euleriteration

    def f(x,y):
        return x**5/y
    assert round(euleriteration(.3, 4, .2, f),5)  == round(4.0001215, 5)
    assert round(euleriteration(1.1, 4.0395341727, .2, f),5) == round(4.119271584547344, 5)

    def g(x,y):
        return -2 + 2*x -2*y
    assert euleriteration(1, 2, .25, g) == 1
    assert euleriteration(1.25, 1, .25, g) == .625

def test_euler():
    from solver.algorithms import euler

    def f(x,y):
        return x**5/y
    assert np.allclose(np.array(euler(.3, .9, 4, 4, f, False)), np.array([(.3, 4), (.5, 4.00012), (.7, 4.00168), (.9, 4.01008)]))
    def g(x,y):
        return -2 + 2*x - 2*y
    assert euler(1, 2, 5, 2, g, False) == [(1, 2), (1.25, 1), (1.5, .625), (1.75, 0.5625), (2, 0.65625)]

def test_improvedeuleriteration():
    from solver.algorithms import improvedeuleriteration

    def f(x,y):
        return x**2/y
    assert round(improvedeuleriteration(.2, 9, .2, f), 5) == 9.00222
    assert round(improvedeuleriteration(.8, 9.01909106791, .2, f), 5) == 9.03726

    def g(x,y):
        return -1 + 2*x - 2*y
    assert improvedeuleriteration(1, -1, .25, g) == -0.375
    assert round(improvedeuleriteration(1.25, -0.375, .25, g),5) == 0.10938

def test_improvedeuler():
    from solver.algorithms import improvedeuler

    def f(x,y):
        return x**2/y
    assert np.allclose(np.array(improvedeuler(.2, .6, 3, 9, f, False)), np.array([(.2, 9), (.4, 9.002222046656572), (.6, 9.00799611837)]))

    def g(x,y):
        return -1 + 2*x - 2*y
    assert np.allclose(np.array(improvedeuler(1, 2, 5, -1, g, False)), np.array([(1, -1), (1.25, -0.375), (1.5, 0.109375), (1.75, 0.505859375), (2, 0.847412109)]))

def test_rungekuttaiteration():
    from solver.algorithms import rungekuttaiteration

    def f(x,y):
        return x**5/y
    assert round(rungekuttaiteration(.3, 6, .2, f),5) == round(6.0004146527867395, 5)
    assert round(rungekuttaiteration(.7, 6.003249126, .2, f),5) == round(6.014727957649027, 5)

    def g(x, y):
        return -1 - 5*x - 2*y
    assert rungekuttaiteration(0, 0, .5, g) == -0.78125
    assert rungekuttaiteration(.5, -0.78125, .5, g) == -1.85546875

def test_rungekutta():
    from solver.algorithms import rungekutta

    def f(x,y):
        return x**5/y
    assert np.allclose(np.array(rungekutta(.3, .7, 3, 6, f, False)), np.array([(.3, 6), (.5, 6.0004146527867395), (.7, 6.003249125657084)]))

    def g(x, y):
        return -1 -5*x - 2*y
    assert np.allclose(np.array(rungekutta(0, 1.5, 4, 0, g, False)), np.array([(0, 0), (.5, -0.78125), (1, -1.85546875), (1.5, -3.039550781)]))

def test_problem1():
    from solver.problem1 import problem1

    s3, s6, s11 = problem1(0, 2, 10)
    assert np.allclose(np.array(s3), np.array([(0, 10), (1, .2), (2, -9.6)]))
    assert (s6[4][1] - s6[1][1])/(s6[4][0] - s6[1][0])  == -9.8 #checking the slope

def test_problem2():
    from solver.problem2 import problem2

    s3, s6, s11 = problem2(0, 2, 5, 15)
    assert s3 == [(0, 5), (1, 20), (2, 35)]
    assert np.isclose((s6[4][1] - s6[1][1])/(s6[4][0] - s6[1][0]), 15) #checking the slope

def test_problem3():
    from solver.problem3 import problem3

    solution1, terminalvelocity1 = problem3(0, 20, 100, 4, 2, True)
    assert round(terminalvelocity1,5) == 2
    assert solution1[0] == (0, 0)
    assert solution1[-1][0] == 20
    assert round(solution1[-10][1], 5) == 2
    assert round(problem3(0, 20, 100, 4, 2, False), 5) == 2

def test_problem4():
    from solver.problem4 import problem4

    assert np.allclose(problem4(0, 20, 50, 50, 1, 1, 101, True)[-1][1], np.zeros(2), atol=1e-05)

def test_problem5():
    from solver.problem5 import problem5

    assert np.allclose(problem5(0, 5, 100, 0, .1, 101, True)[-1][1], np.array([50, 50]))
    assert np.allclose(problem5(3, 5, 120, 20, .25, 101, True)[-1][1], np.array([70, 70]))

def test_problem6():
    from solver.problem6 import problem6

    assert round(problem6(0, 3, 1, 101, 4, 2, True)[-1][1], 3) == 2
    assert round(problem6(2, 4, 2, 101, 5, 1, True)[-1][1], 3) == 5
