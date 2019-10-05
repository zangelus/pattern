
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D


def plot():

    #Parameters to set
    mu_x = 0
    variance_x = 3
    mu_y = 0
    variance_y = 15

    mu_x1 = 2
    variance_x1 = 8
    mu_y1 = 2
    variance_y1 = 8

    #Create grid and multivariate normal
    x = np.linspace(-10,10,500)
    y = np.linspace(-10,10,500)
    X, Y = np.meshgrid(x,y)
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X; pos[:, :, 1] = Y

    rv1 = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])
    rv2 = multivariate_normal([mu_x1, mu_y1], [[variance_x1, 0], [0, variance_y1]])

    rv = rv1

    #Make a 3D plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, rv.pdf(pos),cmap='viridis',linewidth=0)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()
