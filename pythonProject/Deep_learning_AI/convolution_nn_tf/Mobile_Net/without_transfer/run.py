import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import imagenet_utils
import cv2
base_model=tf.keras.applications.MobileNetV2()
def prepared_image(file):
    img=image.load_img(file,target_size=(224,224))
    img=image.img_to_array(img)
    img=np.expand_dims(img,axis=0)
    return tf.keras.applications.mobilenet_v2.preprocess_input(img)
img=prepared_image('picture_sample/img_1.png')
predict=base_model.predict(img)
result=imagenet_utils.decode_predictions(predict)
print(result)