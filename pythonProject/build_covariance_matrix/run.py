import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 8)

# Normal distributed x and y vector with mean 0 and standard deviation 1
x = np.random.normal(0, 1, 500)
y = np.random.normal(0, 1, 500)
X = np.vstack((x, y)).T

plt.scatter(X[:, 0], X[:, 1])

# Covariance
def cov(x, y):
    std_x=np.std(x)
    std_y=np.std(y)
    xbar, ybar = x.mean(), y.mean()
    return (np.sum((x - xbar)*(y - ybar))/(len(x) - 1))/(std_y*std_x)

# Covariance matrix
def cov_mat(X):
    return np.array([[cov(X[0], X[0]), cov(X[0], X[1])],
                     [cov(X[1], X[0]), cov(X[1], X[1])]])

# Calculate covariance matrix
print(cov_mat(X.T)) # (or with np.cov(X.T))