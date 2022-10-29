import numpy as np
import  h5py
from  typical_neuron_network import *
train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig,classes=load_data()
print(train_set_x_orig[0].shape)