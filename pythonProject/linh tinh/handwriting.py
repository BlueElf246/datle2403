import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import os
mnist= tf.keras.datasets.mnist
(x_train,y_train), (x_test,y_test)= mnist.load_data()
# normalizing, scaling down to between 0 and 1
x_train= tf.keras.utils.normalize(x_train, axis=1)
x_test= tf.keras.utils.normalize(x_test, axis=1)
print(x_train.shape)
model= tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28 ,28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
print(model.summary())
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#model.fit(x_train, y_train, epochs=6)
# model.save('handwritten.model')
#
#
# model= tf.keras.models.load_model('../handwritten.model')




# loss, accuracy= model.evaluate(x_test, y_test)
# print( loss, accuracy)
# num=1
# while True:
#     img= cv2.imread(f'digit/number{num}.png')[:, :, 0]
#     img=np.invert(np.array([img]))
#     prediction=model.predict(img)
#     print('the prediction is number ', np.argmax(prediction))
#     plt.imshow(img[0], cmap=plt.cm.binary)
#     plt.show()
#     num+=1
#     if num==10:
#         exit()

