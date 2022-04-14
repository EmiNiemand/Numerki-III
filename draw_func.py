import matplotlib.pyplot as mplot
import numpy as np
import newton_and_knots as nk


def draw_functions(lower_range: float, upper_range: float, function, a: [], c_x: []):
    axes = mplot.figure().subplots()
    x = np.linspace(lower_range, upper_range, 100)
    y = []
    newton_y = []
    for i in x:
        y.append(function(i))
        newton_y.append(nk.newton(a, c_x, i))

    axes.plot(x, y, "r")
    axes.plot(x, newton_y, "b")

    axes.set_xlabel('X')
    axes.set_ylabel('Y')

    mplot.show()

