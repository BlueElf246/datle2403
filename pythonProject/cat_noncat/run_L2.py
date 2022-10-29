import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from dnn_app_utils import *
from nmn import *
train_x_orig, train_y, test_x_orig, test_y, classes = load_data()
# Reshape the training and test examples
train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T   # The "-1" makes reshape flatten the remaining dimensions
test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T
# Standardize seq.txt to have feature values between 0 and 1.
train_x = train_x_flatten / 255.
test_x = test_x_flatten / 255.

layers_dims = [12288,64,64,64,64,64,64,64,64,64,64,64,64, 1]
parameters = L_layer_model(train_x, train_y,layers_dims,learning_rate=0.025, num_iterations=3000, print_cost=True,lambd=0.1)
pred_train = predict(train_x, train_y, parameters)
pred_test = predict(test_x,test_y,parameters)





test_set_x_orig=np.array(test_x_orig)
test_set_y=np.array(test_y).reshape(50,1)
x=np.array(test_set_x_orig)
x_flat=x.reshape(64*64*3,50)
x_flat_test=np.array(x_flat).transpose()
traing_1=[]
for x,y in zip(x_flat_test,test_set_y):
    traing_1.append((np.array(x).reshape(12288,1)/255.,y))
while True:
    num=int(input('type number'))
    if num==100:
        break
    plt.matshow(test_set_x_orig[num])
    plt.show()
    p=predict(traing_1[num][0],traing_1[num][1],parameters)
