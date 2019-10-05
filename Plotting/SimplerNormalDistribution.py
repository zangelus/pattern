import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.mlab import bivariate_normal
from mpl_toolkits.mplot3d import Axes3D

def plot():
  """
    #Parameters to set
    mu_x = 0
    sigma_x = np.sqrt(3)

    mu_y = 0
    sigma_y = np.sqrt(15)

    #Create grid and multivariate normal
    x = np.linspace(-10,10,500)
    y = np.linspace(-10,10,500)
    X, Y = np.meshgrid(x,y)
    Z = bivariate_normal(X,Y,sigma_x,sigma_y,mu_x,mu_y)

    #Make a 3D plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z,cmap='viridis',linewidth=0)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()
   """