import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import seaborn as sns
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df=pd.read_csv(path)
df.to_csv('df.csv')
lm=LinearRegression()
def run1():
    X=df[['highway-mpg']]
    Y=df[['price']]
    lm.fit(X,Y)
    Yhat=lm.predict(X)
    print(Yhat[0:5])
def run2():
    X_test=np.array([5,6,7,8,9])
    X=np.array([0,1,2,3,4])
    Y=np.array([1,3,5,7,9])
    X_test=X_test.reshape(5,1)
    X=X.reshape(5,1)
    Y=Y.reshape(5,1)
    lm.fit(X,Y)
    print(lm.predict(X_test))
    print(lm.coef_,lm.intercept_)
def run3():
    lm1=LinearRegression()
    X=df[['engine-size']]
    Y=df[['price']]
    lm1.fit(X,Y)
    Yhat=lm1.predict(X)
    print(lm1.coef_,lm1.intercept_)
    print('f(x) = ',lm1.coef_,'x + ',lm1.intercept_)
def run4():
    Z=df[['horsepower','curb-weight','engine-size','highway-mpg']]
    lm.fit(Z,df['price'])
    print(lm.intercept_)
    print(lm.coef_)
def run5():
    lm2=LinearRegression()
    Z=df[['normalized-losses','highway-mpg']]
    lm2.fit(Z,df['price'])
    print(lm2.coef_,lm2.intercept_)
# visualize the fiting progress
def run6():
    plt.figure(figsize=(12,10))
    #sns.regplot(x='highway-mpg',y='price',data=df)
    sns.regplot(x="peak-rpm", y="price", data=df)
    plt.ylim(0,)
    plt.show()
def run7():
    Z=df[['peak-rpm','highway-mpg','price']]
    print(Z.corr())
def run8():
    width = 12
    height = 10
    plt.figure(figsize=(width, height))
    sns.residplot(df['highway-mpg'], df['price'])
    plt.show()
def run9():
    lm2 = LinearRegression()
    Z = df[['normalized-losses', 'highway-mpg']]
    lm2.fit(Z, df['price'])
    Y_hat = lm2.predict(Z)
    plt.figure(figsize=(12, 10))

    ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
    sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values", ax=ax1)

    plt.title('Actual vs Fitted Values for Price')
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')

    plt.show()
    plt.close()
def run10():
    r=df[['normalized-losses', 'highway-mpg','price']].corr()
    print(r)
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()
def run12():
    x = df['highway-mpg']
    y = df['price']
    f = np.polyfit(x, y, 11)
    p = np.poly1d(f)
    print(p)
    PlotPolly(p, x, y, 'highway-mpg')
    np.polyfit(x,y,11)
def run13():
    Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
    pr=PolynomialFeatures(degree=2)
    Z_pr=pr.fit_transform(Z)
def run14():
    Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
    Z = Z.astype(float)
    Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)),
             ('model', LinearRegression())]
    pipe = Pipeline(Input)
    y=df['price']
    pipe.fit(Z, y)
    ypipe = pipe.predict(Z)
    print(ypipe[0:4])
def run15():
    Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
    y = df['price']
    Input= [('scale', StandardScaler()),('model',LinearRegression())]
    pipe=Pipeline(Input)
    pipe.fit(Z,y)
    ypipe = pipe.predict(Z)
    print(ypipe[0:10])
run15()
