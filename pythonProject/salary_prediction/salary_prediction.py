import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.metrics import  r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
data=pd.read_csv('data.csv')
# print(seq.txt.isnull().sum())
# print(seq.txt.info())

X = data.drop('Salary',axis=1)
y = data['Salary']
X_train , X_test , Y_train , Y_test = train_test_split(X,y,random_state=101,test_size=0.2)
lr=LinearRegression()
lr.fit(X_train,Y_train)
print(Y_test)
plt.scatter(X_train , Y_train , color='blue')
plt.plot(X_train ,lr.predict(X_train),color='red')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel("Salary")
plt.show()