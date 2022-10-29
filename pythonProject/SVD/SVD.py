import numpy as np
from numpy.linalg import eig
from sympy import *
import os
import matplotlib.image as image
from PIL import Image
import sys
class SVD:
    def input_matrix(self):
        m=int(input('choose number of row'))
        n=int(input('choose number of column'))
        matrix=np.zeros((m,n),dtype=float)
        # input element for matrix
        for x,y in enumerate(matrix):
            for j,k in enumerate(y):
                n=float(input(f'input for element at {x+1},{j+1}'))
                matrix[x][j]=n
        return matrix
    def matrix_multiply(self,matrix1,matrix2):
        new_matrix=np.matmul(matrix1,matrix2)
        return new_matrix
    def matrix_tranpose(self,matrix):
        new_matrix=np.transpose(matrix)
        return new_matrix
    def change_column(self,matrix,value_from, value_to):
        matrix[:,[value_from,value_to]]= matrix[:,[value_to,value_from]]
        return matrix

    def gs1(self,X, row_vecs=True, norm=True):
        if not row_vecs:
            X = X.T
        Y = X[0:1, :].copy()
        for i in range(1, X.shape[0]):
            proj = np.diag((X[i, :].dot(Y.T) / np.linalg.norm(Y, axis=1) ** 2).flat).dot(Y)
            Y = np.vstack((Y, X[i, :] - proj.sum(0)))
        if norm:
            Y = np.diag(1 / np.linalg.norm(Y, axis=1)).dot(Y)
        if row_vecs:
            return Y
        else:
            return Y.T
svd=SVD()
def images(name):
    img=image.imread(name)
    print(img)
def turn_zero(matrix):
    for x,row in enumerate(matrix):
        for y,column in enumerate(row):
            if matrix[x][y]>=0:
                if matrix[x][y]<0.00000000001:
                    matrix[x][y]=0
            else:
                if matrix[x][y]>-0.00000000001:
                    matrix[x][y]=0
def SVD_computation_detail(mat=None):
    matrix=svd.input_matrix()
    # matrix=mat
    # matrix=np.array([[1,0,1],[-2,1,0]])
    # matrix = np.array([[1, 2, 5,2], [3,5, 1,2]])
    print('the matrix to perform SVD')
    print(matrix)
    print('\n')
    matrixT=svd.matrix_tranpose(matrix)
    print(f'tranpose of matrix:\n{matrixT}')
    print('\n')
    print('compute the right singular value:')
    print('ATA is:')
    ATA=svd.matrix_multiply(matrixT, matrix)
    print(ATA)
    print('find the eigen value and eigen vector of ATA')
    w,v=eig(ATA)
    for x,y in enumerate(w):
        if y<0.00000001:
            w[x]=0
    idx=w.argsort()[::-1]
    m=w[idx]
    v=v[:,idx]
    print(f'eigen value:\n {m}')
    print(f'eigen vector:\n {v}')
    m1=np.sqrt(m)
    diagonal_matrix=np.zeros((len(matrix),len(matrix[0])))
    np.fill_diagonal(diagonal_matrix,m1)
    #slice=diagonal_matrix[0:len(matrix)][0:len(matrix[0])]
    sigma_matrix=diagonal_matrix
    right_singular_value=v.transpose()
    # find left singular-value
    u=np.zeros((len(matrix),len(matrix)))
    signal=False
    m1_without_zero=np.trim_zeros(m1)
    for x in range(len(m1_without_zero)):
        u[x]=((svd.matrix_multiply(matrix,v[:,x]))/m1[x])
    k=len(matrix)-len(m1_without_zero)
    if k!=0:
        u=u[:-k,:]
    if len(u)<len(matrix):
        # bay gio tim null space cua u[m]
        a=u
        matrix = Matrix(a)
        m_nullspace = matrix.nullspace()
        k = np.array(m_nullspace).astype(np.float64)
        i = k.transpose()
        final = i[0]
        final1=svd.gs1(final, row_vecs=False).transpose()
        u=np.vstack([u,final1])
    left_singular_value = u.transpose()
    lst=[left_singular_value,sigma_matrix,right_singular_value]
    for x in lst:
        turn_zero(x)
    print('CONCLUSION:\n')
    print('left singular_value\n',left_singular_value,'\n')
    print('sigma_value\n',sigma_matrix,'\n')
    print('right singular_value\n', right_singular_value, '\n')
    return left_singular_value,sigma_matrix,right_singular_value,m1_without_zero
def rank(U,V,m1):
    print(len(m1))
    while True:
        r=int(input('choose rank'))
        if r > len(m1):
            continue
        break
    V_T=V
    U_T=U.transpose()
    matrix=0
    for x in range(r):
        u=np.array([U_T[x]]).transpose()
        v=np.array([V_T[x]])
        matrix+=m1[x]*np.matmul(u,v)
    print(matrix)
    if r==len(m1):
        print('error =',0)
    else:
        print('error =',m1[r]/m1[0])
    return matrix
U,S,V,m1=SVD_computation_detail()
rank(U,V,m1)
# m=Image.open('Google-app-icon-small.png').convert('L')
# m.save('Google-app-icon-small-grey.png')
# gm=image.imread('Google-app-icon-small-grey.png')
# U,S,V,m1=SVD_computation_detail(gm)
# l=rank(U,V, m1)
#
# # img = Image.fromarray(np.uint8(l * 255) , 'L')
# img = Image.fromarray(l , 'L')
# img.save('final.png')
# img.show()
