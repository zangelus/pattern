
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import numpy as np
from scipy.stats import multivariate_normal


def plot():
    
    #Parameters to set
    mu_x = 0
    variance_x = 3
    
    mu_y = 0
    variance_y = 15
    
    x = np.linspace(-10,10,500)
    y = np.linspace(-10,10,500)
    X,Y = np.meshgrid(x,y)
    
    pos = np.array([X.flatten(),Y.flatten()]).T
    
    
    
    rv = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])
    
    
    fig = plt.figure(figsize=(10,10))
    ax0 = fig.add_subplot(111)
    ax0.contour(rv.pdf(pos).reshape(500,500))
    
    
    
    plt.show()