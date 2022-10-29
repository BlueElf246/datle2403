import numpy as np

import mnist_loader
import tensorflow as tf
import matplotlib.pyplot as plt

import network_handwritten
mnist= tf.keras.datasets.mnist
(x_train,y_train),(x_test, y_test)=mnist.load_data()
net = network_handwritten.Neuron_Network([784, 30, 10])
x_train=x_train/255
x_train=np.array(x_train).reshape(60000,784,1)
vectorlize=list()
for y in range(len(y_train)):
    num=y_train[y]
    lst=np.zeros((10,1))
    lst[num]=1.0
    vectorlize.append(lst)
training_data=[(x,y) for x,y in zip(x_train,vectorlize)]

plt.matshow(x_test[0])
plt.show()
x_test=x_test/255
x_test=np.array(x_test).reshape(10000,784,1)
# print(np.array(x_test[0]).shape)
vectorlize1=list()
for y in range(len(y_test)):
    num=y_test[y]
    lst=np.zeros((10,1))
    lst[num]=1.0
    vectorlize1.append(lst)
test_data=[(x,y) for x,y in zip(x_test,vectorlize1)]

net.SGD(training_data , 5, 10, 3.0, test_data=None)


print(np.argmax(net.feedforward(x_test[0])))

print(y_test[0])