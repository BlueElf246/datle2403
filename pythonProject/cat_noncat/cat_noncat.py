import numpy as np
import h5py
import matplotlib.pyplot as plt
import random
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

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
train_set_x_orig=np.array(train_set_x_orig)
train_set_y=np.array(train_set_y).reshape(209,1)
x=np.array(train_set_x_orig)
x_flat=x.reshape(64*64*3,209)
x_flat=np.array(x_flat).transpose()
traing=[]
for x,y in zip(x_flat,train_set_y):
    traing.append((np.array(x).reshape(12288,1)/255,y))
def sigmoid(x):
    return 1/(1+np.exp(-x))
class NN():
    weight_size=np.random.randn(1,12288)
    bias=np.random.randn(1,1)
    def train(self,input, output,ea=0.01):
        #feedforward
        A=sigmoid(np.dot(self.weight_size,input)+self.bias)

        error=output-A
        db=ea*error
        dw=ea*np.dot(error,np.array(input).transpose())
        self.weight_size+=dw
        self.bias+=db
        cost=-(np.dot(output,np.log(A)) + np.dot((1-output),np.log(1 - A)))
        print(cost)
    def run(self,input):
        A = sigmoid(np.dot(self.weight_size, input) + self.bias)
        return A

nn=NN()
for x in range(0,50000):
    rand = random.randint(0, len(traing)-1)
    nn.train(traing[rand][0], traing[rand][1])
# print(nn.weight_size)
# while True:
#     num=int(input('type number'))
#     if num==10:
#         break
#     plt.matshow(train_set_x_orig[num])
#     plt.show()
#     if nn.run(traing[num][0]) >0.9:
#         print('the predictor detect a cat')
#         print(nn.run(traing[num][0]))
#     else:
#         print('this is not a cat picture')
test_set_x_orig=np.array(test_set_x_orig)
test_set_y=np.array(test_set_y).reshape(50,1)
x=np.array(test_set_x_orig)
x_flat=x.reshape(64*64*3,50)
x_flat_test=np.array(x_flat).transpose()
traing_1=[]
for x,y in zip(x_flat_test,test_set_y):
    traing_1.append((np.array(x).reshape(12288,1)/255,y))
while True:
    num=int(input('type number'))
    if num==100:
        break
    plt.matshow(test_set_x_orig[num])
    plt.show()
    if nn.run(traing_1[num][0]) >0.9:
        print('the predictor detect a cat')
        print(nn.run(traing_1[num][0]))
    else:
        print('this is not a cat picture')
        print(nn.run(traing_1[num][0]))

