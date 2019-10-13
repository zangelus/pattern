

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random
   
def plot():
    fig = pyplot.figure()
    ax = Axes3D(fig)

    sequence_containing_x_vals = list(range(-100, 100))
    sequence_containing_y_vals = list(range(-100, 100))
    sequence_containing_z_vals = list(range(-100, 100))
    
    random.shuffle(sequence_containing_x_vals)
    random.shuffle(sequence_containing_y_vals)
    random.shuffle(sequence_containing_z_vals)
    
    ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
    ax.set
    
    pyplot.show()

def scatter3dcolor(x,y,z, cs, colorsMap='jet'):
    cm = plt.get_cmap(colorsMap)
    cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z, c=scalarMap.to_rgba(cs))
    scalarMap.set_array(cs)
    fig.colorbar(scalarMap)
    plt.show()