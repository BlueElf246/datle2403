import tensorflow as tf
import tensorflow.keras.layers as tlf
import h5py
import numpy as np
from PIL import Image
import cv2
from tensorflow.keras.preprocessing import image
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


# 1080,64,64,3     1,1080
def analyze_data(train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig):
    train_x=tf.cast(train_set_x_orig,tf.float32)/255.0
    test_x=tf.cast(test_set_x_orig,tf.float32)/255.0

    train_y=tf.one_hot(train_set_y_orig,depth=6)
    train_y=tf.reshape(train_y,(1080,6))

    test_y=tf.one_hot(test_set_y_orig,depth=6)
    test_y=tf.reshape(test_y,(test_set_y_orig.shape[1],6))

    print(train_x.shape,test_x.shape,train_y.shape,test_y.shape)
    return train_x,train_y,test_x,test_y

def convolutional_layers(input_shape):
    img_shape=tf.keras.Input(shape=input_shape)
    Z1=tlf.Conv2D(filters=64,kernel_size=2,strides=1,padding='same')(img_shape)
    A1=tlf.ReLU()(Z1)
    Max_pool_1=tlf.MaxPool2D(pool_size=2,strides=2,padding='SAME')(A1)
    Z2=tlf.Conv2D(filters=32,kernel_size=2,strides=1,padding='SAME')(Max_pool_1)
    A2 = tlf.ReLU()(Z2)
    Max_pool_2 = tlf.MaxPool2D(pool_size=2, strides=2, padding='SAME')(A2)
    Z3 = tlf.Conv2D(filters=32, kernel_size=2, strides=1, padding='SAME')(Max_pool_2)
    A3 = tlf.ReLU()(Z3)
    Max_pool_3 = tlf.MaxPool2D(pool_size=2, strides=2, padding='SAME')(A3)
    Flatten=tlf.Flatten()(Max_pool_3)
    Output=tlf.Dense(units=6,activation='softmax')(Flatten)
    model=tf.keras.Model(img_shape,Output)
    return model
# prediction = model.predict(newimage)
# print(prediction)
# print(np.argmax(prediction))
def run():
    train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes = load_data()
    train_x, train_y, test_x, test_y = analyze_data(train_set_x_orig, train_set_y_orig, test_set_x_orig,test_set_y_orig)
    model = convolutional_layers((64, 64, 3))
    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    print(model.summary())
    train_data_set=tf.data.Dataset.from_tensor_slices((train_x,train_y)).batch(16)
    test_data_set=tf.data.Dataset.from_tensor_slices((test_x,test_y)).batch(16)
    model.fit(train_data_set,epochs=14,validation_data=test_data_set)
    return model

def picture():
    img_path = 'dat.jpg'
    img = image.load_img(img_path, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0
    return x
model=run()
def cv(model):
    vid=cv2.VideoCapture(0)
    while True:
        ret,frame=vid.read()
        cv2.imshow('frame',frame)
        img=cv2.resize(frame,(64,64),interpolation = cv2.INTER_AREA)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0
        prediction = model.predict(x)
        print(prediction)
        print(np.argmax(prediction))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyWindow()
cv(model)



