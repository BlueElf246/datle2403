import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import random
x_value=[]
y_value=[]
reg=LinearRegression()
for i in range(1000):
    x_value.append(random.randint(0,100))
    y_value.append(random.randint(0,100))
    x=np.array(x_value)
    x=x.reshape(-1,1)

    y = np.array(y_value)
    y = y.reshape(-1, 1)
    if i % 5==0:
        reg.fit(x,y)
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.scatter(x_value,y_value, color='black')
        plt.plot((list(range(100))), reg.predict(np.array([x for x in range(100)]).reshape(-1,1)))
        plt.pause(0.0001)
plt.show()

