import numpy as np
from numpy.linalg import eig
from scipy.linalg import null_space
from sympy import *
from scipy.linalg import qr
import 
def qr_null(A, tol=None):
    Q, R, P = qr(A.T, mode='full', pivoting=True)
    tol = np.finfo(R.dtype).eps if tol is None else tol
    rnk = min(A.shape) - np.abs(np.diag(R))[::-1].searchsorted(tol)
    return Q[:, rnk:].conj()
def matrix_multiply(self, matrix1, matrix2):
    new_matrix = np.matmul(matrix1, matrix2)
    return new_matrix
def input_matrix():
    m=int(input('choose number of row'))
    n=int(input('choose number of column'))
    matrix=np.zeros((m,n),dtype=float)
    # input element for matrix
    for x,y in enumerate(matrix):
        for j,k in enumerate(y):
            n=float(input(f'input for element at {x+1},{j+1}'))
            matrix[x][j]=n
    return matrix

import numpy

def gs_cofficient(v1, v2):
    return numpy.dot(v2, v1) / numpy.dot(v1, v1)

def multiply(cofficient, v):
    return map((lambda x : x * cofficient), v)

def proj(v1, v2):
    return multiply(gs_cofficient(v1, v2) , v1)


def gs1(X, row_vecs=True, norm = True):
    if not row_vecs:
        X = X.T
    Y = X[0:1,:].copy()
    for i in range(1, X.shape[0]):
        proj = np.diag((X[i,:].dot(Y.T)/np.linalg.norm(Y,axis=1)**2).flat).dot(Y)
        Y = np.vstack((Y, X[i,:] - proj.sum(0)))
    if norm:
        Y = np.diag(1/np.linalg.norm(Y,axis=1)).dot(Y)
    if row_vecs:
        return Y
    else:
        return Y.T

#m=np.array([[1,-2,-2]])
m=np.array([[-0.47967118,-0.57236779,-0.66506441]])
matrix=Matrix(m)
m_nullspace=matrix.nullspace()
k=np.array(m_nullspace).astype(np.float64)
print(k)
initial=k[0]
i=k.transpose()
final=i[0]
print(gs1(final,row_vecs=False))