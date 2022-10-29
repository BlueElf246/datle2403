from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(22)

means = [[2, 2], [4, 2]]
cov = [[.3, .2], [.2, .3]]
N = 10
X0 = np.random.multivariate_normal(means[0], cov, N) # class 1
X1 = np.random.multivariate_normal(means[1], cov, N) # class -1
X = np.concatenate((X0.T, X1.T), axis = 1) # all data
print(X)
y = np.concatenate((np.ones((1, N)), -1*np.ones((1, N))), axis = 1) # labels
print(X0.shape)

w =  [-2.00984381,  0.64068336]
b =  4.66856063386812
x_points = np.linspace(-1, 5)    # generating x-points from -1 to 1
y_points = -(w[0] / w[1]) * x_points - b / w[1]  # getting
plt.plot(x_points, y_points, c='r')
plt.scatter(X0.T[0],X0.T[1])
plt.scatter(X1.T[0],X1.T[1])
plt.show()