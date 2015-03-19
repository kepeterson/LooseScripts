from numpy import *
from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3
 
# Linearly Separable
def exampleGraph():
    X1 = rand(50,2) + .3
    X2 = rand(50,2) - .3
    plot(X1[:,0], X1[:,1], 'ro', X2[:,0], X2[:,1], 'bo')
    show()
    return X1, X2
 
# Not linearly separable (using squared features)
def exampleGraph2():
    X1 = (rand(100,2) - .5) * 5
    X2 = (rand(50,2) - .5)
    plot(X1[:,0], X1[:,1], 'bo', X2[:,0], X2[:,1], 'ro')
    show()
    # 3d stuff
    a = vstack([X1[:,0] ** 2, X1[:,1] ** 2, X1[:,0] * X1[:,1]]).T
    b = vstack([X2[:,0] ** 2, X2[:,1] ** 2, X2[:,0] * X2[:,1]]).T
    fig = figure()
    ax = p3.Axes3D(fig)
    ax.plot(a[:,0], a[:,1], a[:,2], 'bo')
    ax.plot(b[:,0], b[:,1], b[:,2], 'ro')
    show()
    return X1, X2
    
exampleGraph2()    