import numpy as np
import copy
from fractions import Fraction
def inp_m(shape=None,num=0,inp=True):
    if shape is None:
        while True:
            try:
                row=int(input('input number of row'))
                col=int(input('input number of col'))
                break
            except:
                continue
    else:
        if type(shape)==int:
            return [num]*shape
        row,col=shape
    new_matrix=[num]*row
    for x,y in enumerate(new_matrix):
        new_matrix[x]=[num]*col
    if inp:
        return new_matrix
    for i in range(row):
        for j in range(col):
            x=int(input(f'input for matrix at {i+1},{j+1}:'))
            new_matrix[i][j]=x
    return new_matrix
def turn_list_to_np_array(lst):
    return np.array(lst)
def matrix_multiplication(matrix1,matrix2):
    new_matrix=[0]*len(matrix1)
    m=1
    n=len(matrix1[0])
    if n==len(matrix2):
        pass
    else: return print('dimension not match')
    if type(matrix2[0])!=int:
        m=len(matrix2[0])
    for x in range(len(new_matrix)):
        new_matrix[x]=[0]*m
    for i,row in enumerate(new_matrix):
        for j,col in enumerate(row):
            sum=0
            for l in range(n):
                sum+=matrix1[i][l]*matrix2[l][j]
            new_matrix[i][j]=sum
    print(f'{turn_list_to_np_array(new_matrix)}')
def transpose(matrix):
    new_matrix=[0]* len(matrix[0])
    m=len(matrix)
    for x in range(len(new_matrix)):
        new_matrix[x]=[0]*m
    for y in range(len(matrix[0])):
        m=[]
        for x in range(len(matrix)):
            m.append(matrix[x][y])
        new_matrix[y]=m
    return  new_matrix
def det(matrix):
    if len(matrix)==len(matrix[0]):
        pass
    else:
        return
def shape(matrix):
    if type(matrix[0])!=list:#vector
        return len(matrix)
    return [len(matrix),len(matrix[0])]
def add_sub(m1,m2,sub=False):
    if shape(m1)==shape(m2):
        new_matrix=inp_m(shape(m1))
        for x,row in enumerate(m1):
            for y,col in enumerate(row):
                if sub:
                    new_matrix[x][y]=m1[x][y] - m2[x][y]
                else:
                    new_matrix[x][y] = m1[x][y] + m2[x][y]
        return new_matrix
    else:
        return 'dim not match'
def prm(matrix):
    for line in matrix:
        print('   '.join(map(str,line)))
def mul_scalar(matrix,scalar):
    for x, row in enumerate(matrix):
            matrix[x]*=scalar
    return matrix
def add_sub_vec(vec1,vec2,sub=False):
    if shape(vec1)==shape(vec2):
        new_matrix=inp_m(shape(vec1))
        for x in range(len(new_matrix)):
            if sub:
                new_matrix[x] = vec1[x] - vec2[x]
                continue
            new_matrix[x]=vec1[x]+vec2[x]
        return new_matrix
    else:
        return 'dim not match'
def vector_transpose(vec):
    for x in range(len(vec)):
        vec[x]=[vec[x]]
    return transpose(vec)

def rref(matrix,det=False,other=True):
    temp1 = copy.deepcopy(matrix)
    temp2=transpose(temp1)
    def func(x):
        if x==-0:
            return 0.0
        else:
            return Fraction(x).limit_denominator()
    for x,line in enumerate(matrix):
        try:
            m=inverse(matrix[x][x])
        except:
            break
        matrix[x]=mul_scalar(matrix[x],m)
        k=0
        if det== True:
            k=x
        for l in range(k,(shape(matrix))[0]):
            if l==x:
                continue
            n=matrix[l][x]/matrix[x][x]
            temp=matrix[x].copy()
            matrix[l]=add_sub_vec(matrix[l],mul_scalar(temp,n),sub=True)
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            matrix[x][y]=func(matrix[x][y])
    if other:
        return matrix
    k=[]
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            if matrix[x][y]==1:
                k.append(y)
    print('if a vector space V is span by a set of vector x:')
    for x in temp2:
        print(x,'.T')
    print('\n')
    print('then the basis of V is/are: ')
    for x in k:
        print(temp2[x],'.T')
    print(f'the dim(v):{len(k)}')

    print('if matrix A is not span of V but it is the transformation matrix such that Ax=y for R^n -> R^m, then:')
    print('the image/range of f(x) at R^m is the span of:')
    for x in k:
        print(temp2[x],'.T')
    print('the kernel/null space such that all x in R^n satisfy Ax=0, where 0 is in R^m is the solution space of Ax=0:')
    temp3 = copy.deepcopy(temp2)
    temp3.append([0] * len(temp2[0]))
    temp3 = transpose(temp3)
    temp3 = rref(temp3)
    prm(temp3)
def inverse(x):
    return 1/x
m1=[[3,2],[2,3],[2,-2]]
m2=[[3,2,2],[2,3,-2]]
# shape(m1)
# matrix_multiplication(np.array([[1,0],[0,1]]),np.array([[-2,1],[1,1]]))
# det(input_matrix((3,2)))
# addition(input_matrix((2,3)),input_matrix((3,2)))
# prm(add_sub(inp_m((3,3),num=1),inp_m((3,3),num=2),sub=True))
# rref(inp_m((3,4),inp=False))
rref(m1,other=False)



