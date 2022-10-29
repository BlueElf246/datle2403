import tensorflow as tf
import tensorflow.keras.layers as tfl
import numpy as np
from tensorflow.keras.initializers import random_uniform, glorot_uniform, constant, identity
import h5py
from tensorflow.keras.layers import Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D
from tensorflow.keras.models import Model, load_model
import matplotlib.pyplot as plt

def load_dataset():
    train_dataset = h5py.File('train_signs.h5', "r")
    # your train set features
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])

    train_set_y_orig = np.array(
        train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('test_signs.h5', "r")
    # your test set features
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])

    test_set_y_orig = np.array(
        test_dataset["test_set_y"][:])  # your test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes
def analyze_data():
    train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes=load_dataset()
    train_set_x=train_set_x_orig
    test_set_x=test_set_x_orig

    train_set_y=tf.one_hot(train_set_y_orig,depth=6,axis=1)
    train_set_y=tf.reshape(train_set_y,(1080,6))
    test_set_y=tf.one_hot(test_set_y_orig,depth=6,axis=1)
    test_set_y=tf.reshape(test_set_y,(test_set_y_orig.shape[1],6))

    train_data_set=tf.data.Dataset.from_tensor_slices((train_set_x,train_set_y)).batch(32)
    test_data_set=tf.data.Dataset.from_tensor_slices((test_set_x,test_set_y)).batch(32)
    return train_data_set,test_data_set
def mobile_net_model(image_shape=(64,64,3)):
    base_model=tf.keras.applications.MobileNetV2(input_shape=image_shape,include_top=False,weights='imagenet')
    #freeze the base model
    base_model.trainable=False
    #create input layer
    input=tf.keras.Input(shape=image_shape)
    preprocessing_input=tf.keras.applications.mobilenet_v2.preprocess_input
    x=preprocessing_input(input)
    x=base_model(x,training=False)
    # use global avg pooling to summarize the info in each channel
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    # include dropout with probability of 0.2 to avoid overfitting
    x=tf.keras.layers.Dropout(0.2)(x)
    output=tfl.Dense(units=6,activation='softmax')(x)
    model=tf.keras.Model(input,output)
    return model
train_data_set,test_data_set=analyze_data()
model=mobile_net_model()
print(model.summary())
model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(train_data_set,validation_data=test_data_set,epochs=20)
