import tensorflow as tf
import tensorflow.keras.layers as tlf
import h5py
import numpy as np
def load_data():
    train_dataset = h5py.File('train_signs.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('test_signs.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # your test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes=load_data()

print(train_set_x_orig.shape)
print(train_set_y_orig.shape)
def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y
def analyze_data(train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig):
    x_train=train_set_x_orig/255.0
    x_test=test_set_x_orig/255.0
    y_train=tf.one_hot(train_set_y_orig,depth=6)
    y_test=tf.one_hot(test_set_y_orig,depth=6)

    y_train=tf.reshape(y_train,(1080,6))
    y_test=tf.reshape(y_test,(len(test_set_y_orig.T),6)) #1080,6

    x_train=x_train.reshape(len(x_train),64*64*3)
    x_test=x_test.reshape(len(x_test),64*64*3)
    print(x_train.shape)
    print(y_train.shape)
    return x_train,y_train,x_test,y_test

x_train,y_train,x_test,y_test= analyze_data(train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig)

def model(input_shape=(12288)):
    input=tf.keras.Input(shape=input_shape)
    L1=tlf.Dense(units=256,activation='relu')(input)
    L2=tlf.Dense(units=256,activation='relu')(L1)
    L3=tlf.Dense(units=128,activation='relu')(L2)
    L4 = tlf.Dense(units=64, activation='relu')(L3)
    L5 = tlf.Dense(units=32, activation='relu')(L4)
    Output=tlf.Dense(units=6,activation='softmax')(L5)
    model=tf.keras.Model(input,Output)
    return model
model=model()
def run(model):
    print(model.summary())
    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    train_data_set = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(16)
    test_data_set = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(16)

    model.fit(train_data_set,epochs=10,validation_data=test_data_set)
run(model)