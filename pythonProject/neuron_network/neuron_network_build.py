import math
import matplotlib.pyplot as plt
import random
import tensorflow as tf
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_prime(x):
    return x*(1-x)
class NeuronNetwork:
    def __init__(self,sizes):# 3,2     2,1            x=3 y=2,     x=2 y=1
        self.weight=[np.random.randn(y,x) for x,y in zip(sizes[:-1], sizes[1:])]
        self.bias=[np.random.randn(x,1) for x in sizes[1:]]
        self.number_layers=len(sizes)
    def feedforward(self,input):
        input=np.array(input).reshape(len(input),1)
        for x,y in zip(self.weight,self.bias):
            input=sigmoid(np.dot(x,input)+y)
        return input
    def cost_function(self,i, target):
        output=self.feedforward(i)
        x = -1*np.array(target*np.log(output)+(1-target)*np.log(1-output))
        x=np.array(x).reshape(len(x),)
        x=np.dot(x,x)
        return x
    def train(self,input, target, ea=0.01):
        input=np.array(input).reshape(len(input),1)
        input_1=input
        activation = [input]
        target = np.array(target).reshape(len(target), 1)
        for x, y in zip(self.weight, self.bias):
            input = sigmoid(np.dot(x, input) + y)
            activation.append(input)
        error=target-input
        self.bias[-1]=self.bias[-1] + ea*error
        self.weight[-1]=self.weight[-1] + ea*np.dot(error,np.array(activation[-2]).transpose())
        for x in range(2,self.number_layers):
            sg=sigmoid_prime(activation[-x])
            error=ea*(np.dot(np.array(self.weight[-x+1]).transpose(),error) * sg)
            self.bias[-x]+=error
            self.weight[-x]+=np.dot(error, np.array(activation[-x-1]).transpose())
        print('cost function is: \n',self.cost_function(input_1,target))

# nn= NeuronNetwork([2,256,256,256,256,1])
# a=[[1,1],[0]]
# b=[[0,0],[0]]
# c=[[1,0],[1]]
# d=[[0,1],[1]]
# lst=[a,b,c,d]
# def doloop():
#     for i in range(50000):
#         rand = random.randint(0, 3)
#         nn.train(lst[rand][0], lst[rand][1])
# doloop()
# print(nn.feedforward([1,0]))
# print(nn.feedforward([0,1]))
# print(nn.feedforward([0,0]))
# print(nn.feedforward([1,1]))

mnist= tf.keras.datasets.mnist
(x_train,y_train),(x_test, y_test)=mnist.load_data()
net = NeuronNetwork([784,256,256,10])
# plt.matshow(x_train[1])
# plt.show()
x_train=x_train/255
x_train=np.array(x_train).reshape(60000,784,1)
vectorlize=list()

for y in range(len(y_train)):
    num=y_train[y]
    lst=np.zeros((10,1))
    lst[num]=1.0
    vectorlize.append(lst)
training_data=[(x,y) for x,y in zip(x_train,vectorlize)]
for x in range(0,50000):
    rand = random.randint(0, len(training_data)-1)
    m,d=training_data[rand]
    net.train(m,d)
x_test_1=x_test
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
count=0
for x in range(0,len(y_test)):
    m,d=test_data[x]
    predict_num=np.argmax(net.feedforward(m))
    if predict_num==y_test[x]:
        count+=1
print(count)

# while True:
#     num=int(input('type number'))
#     if num==10:
#         break
#     plt.matshow(x_test_1[num])
#     plt.show()
#     print('the prediction is',np.argmax(net.feedforward(x_test[num])))

