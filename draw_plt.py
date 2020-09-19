# solve: f(x) = 2x+3
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

from taylor_expansion import taylor, taylor_1


def pltUsingfunc(min=-5, max=5, step=0.5):
    xarray = []
    yarray = []
    for x in np.arange(min, max, step):
        y = 2*x + 3
        xarray.append(x)
        yarray.append(y)
    # Plot the data
    plt.plot(xarray, yarray, label='2x+3')
    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.grid(True)
    plt.title('f(x) = 2x+3')
    # Show the plot
    plt.show()

def pltUsingTaylerExp():
    x = sy.Symbol('x')
    f = 2 * x + 3
    #using taylor expansion
    x_lims = [-5, 5]
    x1 = np.linspace(x_lims[0], x_lims[1], 800)
    y1 = []
    # Approximate up until 10 starting from 1 and using steps of 2
    for j in np.arange(1, 10, 1):
        func = taylor(f, 0, j)
        print('Taylor expansion at n=' + str(j), func)
        for k in x1:
            y1.append(func.subs(x, k))
        plt.plot(x1, y1, label='order ' + str(j))
        y1 = []
    # Plot the function to approximate (2x+3, in this case)
    plt.xlim(x_lims)
    plt.ylim([-5, 5])
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.grid(True)
    plt.title('Taylor series approximation of f(x) = 2x+3')
    plt.show()


if __name__ == "__main__":
    pltUsingfunc()
    pltUsingTaylerExp()
    # This will plot sine and its Taylor approximations
    # from sympy.functions import sin
    #
    # x = sy.Symbol('x')
    # p = plt.plot(sin(x), taylor(sin(x), 0, 1), taylor(sin(x), 0, 3), taylor(sin(x), 0, 5),
    #          (x, -3.5, 3.5))
    #
    # p[0].line_color = 'blue'
    # p[1].line_color = 'green'
    # p[2].line_color = 'firebrick'
    # p[3].line_color = 'black'
    # p.title = 'Taylor Series Expansion for Sine'
    # p.show()
