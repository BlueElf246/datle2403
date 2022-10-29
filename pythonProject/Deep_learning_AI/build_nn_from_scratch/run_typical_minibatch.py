import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from dnn_app_utils import *
from typical_nn_with_minibatch_gd_momentum_adam import *
train_x_orig, train_y, test_x_orig, test_y, classes = load_data()
# Reshape the training and test examples
train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T   # The "-1" makes reshape flatten the remaining dimensions
test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T

# Standardize seq.txt to have feature values between 0 and 1.
train_x = train_x_flatten / 255.
test_x = test_x_flatten / 255.

# minibatches = random_mini_batches(train_x, train_y, mini_batch_size=64)
# for minibatch in minibatches:
#     mini_X,mini_Y=minibatch
#     print(mini_X.shape,mini_Y.shape)

layers_dims = [12288,64,64,64,64,32,1]
parameters = model(train_x, train_y,layers_dims,learning_rate=0.0007,optimizer='adam',num_epochs=500,mini_batch_size=64,print_cost=True)
pred_train = predict(train_x, train_y, parameters)
pred_test = predict(test_x,test_y,parameters)

