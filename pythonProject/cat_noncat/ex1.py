import random
import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from dnn_app_utils import *

import model_ex
train_x_orig, train_y, test_x_orig, test_y, classes = load_data()
# Reshape the training and test examples
train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T   # The "-1" makes reshape flatten the remaining dimensions
test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T
class save():
    parameters=dict()
hi=save()
# Standardize seq.txt to have feature values between 0 and 1.
train_x = train_x_flatten / 255.
test_x = test_x_flatten / 255.


m=[]
special=np.array(train_x).reshape(209,12288)
for x in range(np.array(special).shape[0]):
    x=np.array(special[x]).reshape(12288,1)
    m.append(x)
layers_dims = [12288, 20, 7, 5, 1]
for x in range(0,5000):
    num=random.randint(0,208)
    parameters,cost = model_ex.L_layer_model(m[num], train_y[0][num],layers_dims,learning_rate=0.0075, num_iterations=1, print_cost=True)
    # pred_test = dnn_app_utils.predict(train_x, train_y, parameters)
    hi.parameters=parameters
    print(cost)



# train_set_x_orig=np.array(train_x_orig)
# train_set_y=np.array(train_y).reshape(209,1)
# x=np.array(train_set_x_orig)
# x_flat=x.reshape(64*64*3,209)
# x_flat=np.array(x_flat).transpose()
# traing=[]
# for x,y in zip(x_flat,train_set_y):
#     traing.append((np.array(x).reshape(12288,1)/255.,y))

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
my_image = "my_image.jpg" # change this to the name of your image file
my_label_y = [1] # the true class of your image (1 -> cat, 0 -> non-cat)
## END CODE HERE ##v5

fname = "images/" + my_image
image = np.array(Image.open(my_image).resize((64, 64)))
plt.imshow(image)
plt.show()
image = image / 255.
image = image.reshape((1, 64 * 64 * 3)).T
print(np.array(image).shape)
my_predicted_image =predict(image, my_label_y, parameters)


print ("y = " + str(np.squeeze(my_predicted_image)) + ", your L-layer model predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")