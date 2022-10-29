import h5py
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow.keras.layers as tfl
def load_dataset():
    train_set=h5py.File('train_happy.h5','r')
    test_set=h5py.File('test_happy.h5','r')
    train_set_x= np.array(train_set['train_set_x'][:])
    train_set_y=np.array(train_set['train_set_y'][:])
    test_set_x=np.array(test_set['test_set_x'][:])
    test_set_y = np.array(test_set['test_set_y'][:])

    train_set_y=train_set_y.reshape(1,train_set_x.shape[0])
    test_set_y=test_set_y.reshape(1,test_set_x.shape[0])
    return train_set_x,train_set_y,test_set_x,test_set_y
def show_pic(index,train_org):
    plt.imshow(train_org[index])
    plt.show()
train_x_org,train_y,test_x_org,test_y=load_dataset()
print(train_x_org.shape,train_y.shape) #600 training example, each ex.shape= 64,64,3

#normalize the image vector
train_x=train_x_org/255.0
test_x=test_x_org/255.0

train_y=train_y.T
test_y=test_y.T

def model():
    model=tf.keras.Sequential([tfl.ZeroPadding2D((3,3),input_shape=(64,64,3)),
                               tfl.Conv2D(filters=32,kernel_size=7,strides=1),
                               tfl.BatchNormalization(axis=3),
                               tfl.ReLU(),
                               tfl.MaxPool2D(),
                               tfl.Flatten(),
                               tfl.Dense(1,activation='sigmoid')])
    return model
happy_model=model()
print(happy_model.summary())
happy_model.compile(optimizer='Adam',loss='binary_crossentropy',metrics='accuracy')
happy_model.fit(train_x,train_y,epochs=10,batch_size=16)
happy_model.evaluate(test_x,test_y)
#
# happy_model.save('happy_face.model')








