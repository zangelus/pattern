#%%setup

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def plot():
    x =  np.linspace(0,20,100)
    plt.plot(x,np.sin(x))
    plt.show()