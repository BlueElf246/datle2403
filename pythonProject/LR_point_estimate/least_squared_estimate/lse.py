import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
d={'x':[132.0,129.0,120.0,113.2,105.0,92.0,84.0,83.2,88.4,59.0,80.0,81.5,71.0,69.2],
   'y':[46.0,48.0,51.0,52.1,54.0,52.0,59.0,58.7,61.6,64.0,61.4,54.6,58.8,58.0]
   }
df=pd.DataFrame(data=d)


def prepresent(x_present,yhat,y_observed):
    plt.xlim([x_present.min(),x_present.max()])
    plt.ylim([y_observed.min(), y_observed.max()])
    plt.plot(x_present,y_observed, 'x')
    plt.plot(x_present, yhat)
    plt.show()
def variance(x_present,yhat,y_observed):
    SSE = sum((y_observed - yhat) ** 2)  # residual^2
    v = SSE / len(x_present)
    return v
def RMSE(x_present,yhat,y_observed): # compare error dataset, same scale and same unit of y
    v=variance(x_present,yhat,y_observed)
    RMSE=np.sqrt(v)
    return RMSE
def r2(x_present,yhat,y_array):
    mean = np.mean(y_array)
    SST = sum((y_array - mean) ** 2)
    SSE = sum((y_array - yhat) ** 2)
    r2=1-(SSE/SST)
    return r2
def polynimial(degree=1,regulizer=None):
    df['x_0']=np.full((14,1),1)
    # estimate parameter using least square estimate
    for x in range(1,degree+1):
        df[f'x_{x}']=df['x']**x
    lst=df.columns.tolist()
    n=['x','y']
    lst=[ele for ele in lst if ele not in n]
    x_array=df[lst].to_numpy()
    y_array=df[['y']].to_numpy()
    x_array_trans = x_array.reshape(len(x_array[0]), len(x_array))
    XTX = np.matmul(x_array_trans, x_array)
    if regulizer!=None:
        r=np.zeros((len(XTX),len(XTX[0])))
        np.fill_diagonal(r,regulizer)
        XTX+=r
    inverse = np.linalg.inv(XTX)
    XTy = np.matmul(x_array_trans, y_array)
    final = np.matmul(inverse, XTy)
    d={}
    for x in range(0,degree+1):
        d["x_{0}".format(x)]=f'x_{x}'
    for x in range(0,degree+1):
        d["x_{0}".format(x)]=df[[d["x_{0}".format(x)]]].to_numpy()
    yhat=0
    for x in range(degree,-1,-1):
        yhat+=final[x][0]*d[f'x_{x}']
    yhat_present = np.array(yhat).transpose()[0]
    x_present = df['x'].to_numpy()
    y_observed = np.array(y_array).transpose()[0]
    print(f'for degree: {degree}')
    v=variance(x_present,yhat_present,y_observed)
    RMSE1= RMSE(x_present,yhat_present,y_observed)
    print(f'variance is: {v}')
    print(f'RMSE is :{RMSE1}')
    if degree==1:
        print(f'r2 score is:{r2(x_present,yhat_present,y_observed)}')
    print(final)
    prepresent(x_present, yhat_present, y_observed)
for x in range(1,14):
    polynimial(degree=x)
