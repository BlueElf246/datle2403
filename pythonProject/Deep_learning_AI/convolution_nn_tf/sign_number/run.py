import numpy as np
import tensorflow as tf
import tensorflow.keras.layers as tlf
import pandas as pd
import h5py
import matplotlib.pyplot as plt
def train_set():
    df = pd.read_csv('sign_mnist_train.csv')
    label = df.pop('label')
    x_train = np.array(df)
    y_train = np.array(label).reshape(27455, 1)
    x_train = x_train.reshape((27455, 28, 28))
    y_train = tf.one_hot(y_train, depth=26, axis=1)
    y_train = tf.reshape(y_train, (27455, 26))
    return x_train,y_train
def test_set():
    df=pd.read_csv('sign_mnist_test.csv')
    label = df.pop('label')
    x_test = np.array(df)
    y_test = np.array(label).reshape(7172, 1)
    x_test = x_test.reshape((7172, 28, 28))
    y_test = tf.one_hot(y_test, depth=26, axis=1)
    y_test = tf.reshape(y_test, (7172, 26))
    return x_test,y_test
def load_dataset():
    train_dataset = h5py.File('../convolution_nn_tf/Res_Net/train_signs.h5', "r")
    # your train set features
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])

    train_set_y_orig = np.array(
        train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('../convolution_nn_tf/Res_Net/test_signs.h5', "r")
    # your test set features
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])
    test_set_y_orig = np.array(
        test_dataset["test_set_y"][:])  # your test set labels
    classes = np.array(test_dataset["list_classes"][:])  # the list of classes
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

x_train,y_train=train_set()
x_test,y_test=test_set()

print(x_train.shape,y_train.shape)
def convolutional_layers(input_shape):
    img_shape=tf.keras.Input(shape=input_shape)
    Z1=tlf.Conv1D(filters=16,kernel_size=2,strides=1,padding='same')(img_shape)
    A1=tlf.ReLU()(Z1)
    Max_pool_1=tlf.MaxPool1D(pool_size=2,strides=2,padding='SAME')(A1)
    Z2=tlf.Conv1D(filters=32,kernel_size=2,strides=1,padding='SAME')(Max_pool_1)
    A2 = tlf.ReLU()(Z2)
    Max_pool_2 = tlf.MaxPool1D(pool_size=2, strides=2, padding='SAME')(A2)
    Flatten=tlf.Flatten()(Max_pool_2)
    Output=tlf.Dense(units=26,activation='softmax')(Flatten)
    model=tf.keras.Model(img_shape,Output)
    return model
def run():
    model=convolutional_layers((28,28))
    model.compile(optimizer='Adam',metrics=['accuracy'],loss='categorical_crossentropy')
    print(model.summary())
    train_data_set=tf.data.Dataset.from_tensor_slices((x_train,y_train)).batch(64)
    test_data_set=tf.data.Dataset.from_tensor_slices((x_test,y_test)).batch(64)
    model.fit(train_data_set,epochs=200,validation_data=test_data_set)














