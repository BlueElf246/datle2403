import math
import matplotlib.pyplot as plt
import random
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_prime(x):
    return x*(1-x)
import h5py
def load_dataset():
    train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # your test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes
count=1
class NeuronNetwork:
    h_1=[]
    count_1=1
    def __init__(self,sizes):# 3,2     2,1            x=3 y=2,     x=2 y=1
        self.weight=[np.random.randn(y,x) for x,y in zip(sizes[:-1], sizes[1:])]
        self.bias=[np.random.randn(x,1) for x in sizes[1:]]
        self.number_layers=len(sizes)
        self.batch_w_1 = [np.zeros(w.shape) for w in self.weight]
        self.batch_b_1 = [np.zeros(b.shape) for b in self.bias]
    def feedforward(self,input):
        input=np.array(input).reshape(len(input),1)
        for x,y in zip(self.weight,self.bias):
            input=sigmoid(np.dot(x,input)+y)
        return input
    def cost_function(self,i, target,m):
        A2=self.feedforward(i)
        Y=target
        logprobs = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2))
        cost = -np.sum(logprobs) / m
        cost = float(np.squeeze(cost))

        return cost
        # output=self.feedforward(i)
        # # x = -1/m*np.array(target*np.log(output)+(1-target)*np.log(1-output))
        # # x=np.array(x).reshape(len(x),1)
        # x=(target-output)**2
        # x=np.sum(x,axis=1)
        # return x
    def train(self,input, target, eta, training_ex=1):
        input=np.array(input).reshape(len(input),1)
        activation = [input]
        target = np.array(target).reshape(len(target), 1)
        for x, y in zip(self.weight, self.bias):
            input = sigmoid(np.dot(x, input) + y)
            activation.append(input)
        batch_w=[np.zeros(w.shape) for w in self.weight]
        batch_b=[np.zeros(b.shape) for b in self.bias]
        dz=activation[-1]-target
        dw=(1/training_ex)* np.dot(dz,np.array(activation[-2]).transpose())
        db=(1/training_ex)* np.sum(dz,axis=1,keepdims=True)
        # self.bias[-1]=self.bias[-1] - ea*error
        # self.weight[-1]=self.weight[-1] - ea*np.dot(error,np.array(activation[-2]).transpose())
        batch_w[-1]=dw
        batch_b[-1]=db
        for x in range(2,self.number_layers):
            sg=sigmoid_prime(activation[-x])
            dz=np.multiply(np.dot(self.weight[-x+1].transpose(), dz),sg)
            dw=(1/training_ex)*np.dot(dz,np.array(activation[-x-1]).transpose())
            db=(1/training_ex)*np.sum(dz,axis=1,keepdims=True)
            batch_w[-x]=dw
            batch_b[-x]=db
            # error=ea*(np.dot(np.array(self.weight[-x+1]).transpose(),error) * sg)
            # self.bias[-x]-=error
            # self.weight[-x]-=np.dot(error, np.array(activation[-x-1]).transpose())
        return batch_w,batch_b
    def mini_batch(self,count,training, eta, training_ex):
        num=random.randint(0,208)
        input,target=training[num]
        input_1=input
        # if self.count_1%10!=0 and self.count_1!=500:
        #     batch_w, batch_b = self.train(input, target, eta, training_ex)
        #     self.batch_b_1=[b_1+b for b_1,b in zip(self.batch_b_1,batch_b)]
        #     self.batch_w_1=[w_1+w for w_1,w in zip(self.batch_w_1,batch_w)]
        #     self.count_1+=1
        #     self.mini_batch(self.count_1,training,0.01,training_ex)
        # elif self.count_1%10==0 and self.count_1!=500:
        #     self.weight = [w - (eta * nw) for w, nw in zip(self.weight, self.batch_w_1)]
        #     self.bias = [b - (eta * nb) for b, nb in zip(self.bias, self.batch_b_1)]
        #     h = self.cost_function(input_1, target,training_ex)
        #     print('done epochs',self.count_1/10 ,'cost function is: \n', h)
        #     self.h_1.append((h,self.count_1/10))
        #     self.batch_w_1 = [np.zeros(w.shape) for w in self.weight]
        #     self.batch_b_1 = [np.zeros(b.shape) for b in self.bias]
        #     self.count_1 += 1
        #     self.mini_batch(self.count_1, training, 0.01, training_ex)
        # elif self.count_1==500:
        #     return self.h_1
        batch_w, batch_b = self.train(input, target, eta, training_ex)
        self.weight = [w - (eta * nw) for w, nw in zip(self.weight, batch_w)]
        self.bias = [b - (eta * nb) for b, nb in zip(self.bias, batch_b)]
        self.count_1+=1
        if self.count_1 %1==0:
            return (self.cost_function(input_1,target,training_ex))
        return None



train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
train_set_x_orig=np.array(train_set_x_orig)
train_set_y=np.array(train_set_y).reshape(209,1)
x=np.array(train_set_x_orig)
x_flat=x.reshape(64*64*3,209)
x_flat=np.array(x_flat).transpose()
traing=[]

for x,y in zip(x_flat,train_set_y):
    traing.append((np.array(x).reshape(12288,1)/255,y))
print(traing[2])
# nn=NeuronNetwork([12288,6144,3072,768,192,96,1])
# traing_ex=(np.array(train_set_y).shape)[0]
# for x in range(0,2000):
#     cost=nn.mini_batch(1,traing,0.1,traing_ex)
#     if cost is None:
#         continue
#     print(cost)
#     plt.scatter(x,cost,color='red')
# # plt.ylim(0,0.05)
# plt.show()
#
# test_set_x_orig=np.array(test_set_x_orig)
# test_set_y=np.array(test_set_y).reshape(50,1)
# x=np.array(test_set_x_orig)
# x_flat=x.reshape(64*64*3,50)
# x_flat_test=np.array(x_flat).transpose()
# traing_1=[]
# for x,y in zip(x_flat_test,test_set_y):
#     traing_1.append((np.array(x).reshape(12288,1)/255,y))
# # while True:
# #     num=int(input('type number'))
# #     if num==100:
# #         break
# #     plt.matshow(train_set_x_orig[num])
# #     plt.show()
# #     if nn.feedforward(traing[num][0]) >0.9:
# #         print('the predictor detect a cat')
# #         print(nn.feedforward(traing[num][0]))
# #     else:
# #         print('this is not a cat picture')
# #         print(nn.feedforward(traing[num][0]))
while True:
    num=int(input('nhap so:'))
    plt.matshow(train_set_x_orig[num])
    plt.show()
    # print(nn.feedforward(traing[num][0]))
