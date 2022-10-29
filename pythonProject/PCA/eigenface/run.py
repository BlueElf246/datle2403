import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import imageio
states = ['centerlight', 'glasses', 'happy', 'leftlight',
          'noglasses', 'normal', 'rightlight','sad',
          'sleepy', 'surprised', 'wink' ]
prefix = 'subject'
lst=[]

for x in states:
    for i in range(1,16):
        if i <10:
            m='0'+str(i)
        else:
            m=i
        file=f'data/subject{m}.{x}'
        image = imageio.imread(file)
        lst.append(image)
lst=np.array(lst)
# print(lst[0].shape)
# plt.imshow(lst[0])
# plt.show()
# print(lst.shape)
# print(lst[0])
image=lst[0]
#PCA a single picture
def present(X):
    plt.imshow(X)
    plt.show()
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
    # print(Z.shape)
    # print('')
    # print(Z)
    # we present sample in X as column,
    X=X.T
    reconst = (projection_matrix(B) @ X)
    # x=X
    # present(x[0],x[1],reconst.T)
    #unnormailize the dataset
    reconstruction=reconst.T*std+mu
    return reconstruction
# for x in range(10,110,20):
#     i=PCA(image,x)
#     present(i)
PCA(image,2)

