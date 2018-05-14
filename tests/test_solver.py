
def test_validinput():
    from solver.algorithms import validinput

    assert validinput(5, 0, 12) == False
    assert validinput(0, 5, 1.2) == False
    assert validinput(0, 5, 4) == True

def test_euleriteration():
    from solver.algorithms import euleriteration

    def f(x,y):
        return x**5/y
    assert euleriteration(.3, 4, .2, f),  == 4.0001215
    assert euleriteration(1.1, 4.0395341727, .2, f) == 4.119271584547344

    def g(x,y):
        return -2 + 2*x -2*y
    assert euleriteration(1, 2, .25, g) == 1
    assert euleriteration(1.25, 1, .25, g) == .625

def test_euler():
    from solver.algorithms import euler

    def f(x,y):
        return x**5/y
    assert euler(.3, .9, 4, 4, f, False) == [(.3, 4), (.5, 4.0001215), (.7, 4.001683952540504), (.9, 4.010083916255445)]
    def g(x,y):
        return -2 + 2*x - 2*y
    assert euler(1, 1.2, 5, 2, f, False) == [(1, 2), (1.25, 1), (1.5, .625), (1.75, 0.5625), (2)]

def test_improvedeuleriteration():
    from solver.algorithms import improvedeuleriteration

    def f(x,y):
        return x**2/y
    assert improvedeuleriteration(.2, 9, .2, f) == 9.002222046656572
    assert improvedeuleriteration(.8, 9.01909106791, .2, f) == 9.037257298806503

    def g(x,y):
        return -1 + 2*x - 2*y
    assert improvedeuleriteration(1, -1, .25, g) == -0.375
    assert improvedeuleriteration(1.25, -0.375, .25, g) == 0.109375

def test_improvedeuler():
    from solver.algorithms import improvedeuler

    def f(x,y):
        return x**2/y
    assert improvedeuler(.2, 1.2, 3, 9, f, False) == [(.2, 9), (.4, 9.002222046656572), (.6, 9.00799611837)]

    def g(x,y):
        return -1 + 2*x - 2*y
    assert improvedeuler(1, 2, 5, -1, g, False) == [(1, -1), (1.25, -0.375), (1.5, 0.109375), (1.75, 0.505859375), (2, 0.847412109)]

def test_rungekuttaiteration():
    from solver.algorithms import rungekuttaiteration

    def f(x,y):
        return x**5/y
    assert rungekuttaiteration(.3, 6, .2, f) == 6.0004146527867395
    assert rungekuttaiteration(.7, 6.003249126, .2, f) == 6.014727957649027

    def g(x, y):
        return -1 - 5*x - 2*y
    assert rungekuttaiteration(1, -1, .5, g) == -0.375
    assert rungekuttaiteration(1.25, -0.375, .5, g) == 0.109375

def test_rungekutta():
    from solver.algorithms import rungekutta

    def f(x,y):
        return x**5/y
    assert rungekutta(.3, .7, 3, 6, f, False) == [(.3, 6), (.5, 6.0004146527867395), (.7, 6.003249125657084)]

    def g(x, y):
        return -1 -5*x - 2*y
    assert rungekutta(0, 1.5, 4, 0, g, False) == [(0, 0), (.5, -0.78125), (1, -1.85546875), (1.5, -3.039550781)]

def test_problem1():

def test_problem2():

def test_problem3():

def test_problem4():

def test_problem5():

def test_problem6():
