import numpy as np
import matplotlib.pyplot as plt
d={'x':[132.0,129.0,120.0,113.2,105.0,92.0,84.0,83.2,88.4,59.0,80.0,81.5,71.0,69.2],
   'y':[46.0,48.0,51.0,52.1,54.0,52.0,59.0,58.7,61.6,64.0,61.4,54.6,58.8,58.0]
   }
x=np.array(d['x'])
y=np.array(d['y'])
X=np.array([x,y]).T
def present(x,y,reconst):
    x_re,y_re=reconst.T[0],reconst.T[1]
    plt.plot(x_re, y_re, 'o')
    plt.xlim([x.min(), x.max()])
    plt.ylim([y.min(), y.max()])
    plt.plot(x, y, 'x')

    plt.show()
#STEP IN PCA
# 1/ standardize the dataset, i.e: make mean=0 and std=1
def normalize(X):
    mu=np.mean(X,axis=0) # compute the mean of each feature
    std=np.std(X,axis=0) # compute the std of each feature
    std[std==0]=1.0
    X_bar=(X-mu)/std
    return X_bar,mu,std
# 2/ find eigen value and eigen vector of Covariance matrix
def eign(S):
    eigvals, eigvecs = np.linalg.eig(S)
    k = np.argsort(eigvals)[::-1]
    return eigvals[k], eigvecs[:, k]
def projection_matrix(B):
    return (B @ B.T)
def PCA(X,num_components):
    X,mu,std=normalize(X)
    S=1.0/len(X)*np.dot(X.T,X)
    eigen_value,eigen_vector=eign(S)
    eigen_value = eigen_value[:num_components]
    eigen_vector = eigen_vector[:, :num_components]
    B = np.real(eigen_vector)
    Z=((B.T@X.T))
    print(Z.shape)
    print('')
    print(Z)
    # we present sample in X as column,
    X=X.T
    reconst = (projection_matrix(B) @ X)
    # x=X
    # present(x[0],x[1],reconst.T)
    #unnormailize the dataset
    reconstruction=reconst.T*std+mu
    return reconstruction
(PCA(X,1))
#present(x,y,PCA(X,1))
# S=np.array([[5/4,0,0,-5/4],[0,5/4,-5/4,0],[0,-5/4,5/4,0],[-5/4,0,0,5/4]])
# print(eign(S))
